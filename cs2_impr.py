import executable 
import reveal_globals
import time
import  copy
import psycopg2
import psycopg2.extras
import error_handler

def getCoreSizes_cs(core_relations):
    core_sizes = {}
    for table in core_relations:
        cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('select count(*) from ' + table + ';')
        res = cur.fetchone()
        cnt = int(str(res[0]))
        core_sizes[table] = cnt
    reveal_globals.global_core_sizes= core_sizes


def correlated_sampling_start():
    itr=5
    cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    getCoreSizes_cs(reveal_globals.global_core_relations)
    
    for table in reveal_globals.global_core_relations:
        cur.execute("alter table " + table + " rename to " + table + "_tmp;")
    cur.close()
    #restore original tables somewhere
    start_time=time.time()
    while itr>0:
        if correlated_sampling()== False:
            print('sampling failed in iteraation', itr)
            itr = itr-1
        else:
            cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            for table in reveal_globals.global_core_relations:
                cur.execute("drop table " + table + "_tmp;")
            cur.close()
            reveal_globals.cs_time = time.time() - start_time
            print("CS PASSED")
            return

    print("correlated samplin failed totally starting with halving based minimization")
    cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for table in reveal_globals.global_core_relations:
        cur.execute("alter table " + table + "_tmp rename to " + table + " ;")
    cur.close()
    # cs sampling time
    reveal_globals.cs_time = time.time() - start_time
    return

            
def correlated_sampling():
    print(reveal_globals.global_key_lists)
    print("Starting correlated sampling ")
    
    temp_global_key_list= copy.deepcopy(reveal_globals.global_key_lists)
    seed_sample_size_per=1
    
    not_sampled_tables=copy.deepcopy(reveal_globals.global_core_relations)
    
    for table in not_sampled_tables:
        if reveal_globals.global_core_sizes[table] < 100:
            not_sampled_tables.remove(table)

    cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for table in reveal_globals.global_core_relations:
        cur.execute("create table " + table + " (like " + table + "_tmp);")
    cur.close()
    # choose base table from each key list> sample it> sample remaining tables based on base table
    # for first key_list 
    # for remaining key list choose base table as some already sampled table
    for key_list in temp_global_key_list:
        max_cs = 0
        # allsampled = True 
        for i in range(0,len(key_list)):
            if max_cs < reveal_globals.global_core_sizes[key_list[i][0]] :
                max_cs = reveal_globals.global_core_sizes[key_list[i][0]]
                base_t = i
                # break
                # allsampled = False
                  
        # Sample base table      
        base_table = key_list[base_t][0]
        base_key=key_list[base_t][1]
        limit_row= reveal_globals.global_core_sizes[ base_table ]
        cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print("insert into "+ base_table +" select * from "+base_table+"_tmp tablesample system(" + str(seed_sample_size_per) + ") where ("+base_key+") not in (select distinct("+base_key+") from " + base_table +")  Limit " + limit_row + " ;")
        cur.execute("insert into "+ base_table +" select * from "+base_table+"_tmp tablesample system(" + str(seed_sample_size_per) + ") where ("+base_key+") not in (select distinct("+base_key+") from "+ base_table +")  Limit " + limit_row + " ;")
        cur.close()
        # cur = reveal_globals.global_conn.cursor()
        # cur.execute("select count(*) from " + base_table + ";")
        # res = cur.fetchone()
        # print(base_table, res)
        # sampled_tables.append(base_table)
        # not_sampled_tables.remove(base_table)
        
        # sample remaining tables from key_list using the sampled base table
        for i in range(0,len(key_list)):
            print(i)
            tabname2 = key_list[i][0]
            key2 = key_list[i][1]
            
            # if tabname2 in not_sampled_tables:
            if tabname2 != base_table:
                limit_row= reveal_globals.global_core_sizes[ tabname2 ]
                cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                print("insert into " + tabname2 + " select * from "+tabname2+"_tmp where " + key2 + " in (select distinct(" + base_key + ") from "+base_table+") and "+ key2 + " not in (select distinct("+key2+") from "+tabname2+") Limit " + limit_row + " ;")
                cur.execute("insert into " + tabname2 + " select * from "+tabname2+"_tmp where " + key2 + " in (select distinct(" + base_key + ") from " + base_table + ") and " + key2 + " not in (select distinct(" + key2 + ") from " + tabname2 + " ) Limit " + limit_row + " ;")
                cur.close()                    
                # cur = reveal_globals.global_conn.cursor()
                # cur.execute("select count(*) from " + tabname2 + ";")
                # res = cur.fetchone()
                # print(tabname2, res)
                # sampled_tables.append(tabname2)
                # not_sampled_tables.remove(tabname2)
        
    if len(temp_global_key_list) == 0:
        for table in not_sampled_tables:
            cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            print("insert into "+ table +" select * from "+ table +"_tmp tablesample system(" + str(seed_sample_size_per) + ");")
            cur.execute("insert into "+ table +" select * from "+ table +"_tmp tablesample system(" + str(seed_sample_size_per) + ");")
            cur.close()
            cur = reveal_globals.global_conn.cursor()
            cur.execute("select count(*) from " + table + ";")
            res = cur.fetchone()
            print(table, res)

    # count rows after sampling
    for table in reveal_globals.global_core_relations:
        cur = reveal_globals.global_conn.cursor()
        cur.execute("select count(*) from " + table + ";")
        res = cur.fetchone()
        print(table, res)


    new_result= executable.getExecOutput()
    if len(new_result)<=1:
        print('sampling failed in iteraation')
        cur = reveal_globals.global_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        for table in reveal_globals.global_core_relations:
            cur.execute("drop table " + table + ";")
        cur.close()
        return False
    else:
        # drop original tables
        # convert views to tables 
        return True

	


