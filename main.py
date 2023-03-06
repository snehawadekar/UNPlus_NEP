#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Mar 21, 2020 10:05:19 AM IST  platform: Windows NT

# from google.cloud.sql.connector import connector
# import google.cloud.sql.connector.pg8000 as pg8000
# import pg8000
#new reveal.py = reveal.py + reveal_support.py + reveal_proc.py + reveal_proc_support.py
# import mysql.connector

#newcomment git check
import psycopg2
from pickle import TRUE
from flask import *
import csv
import sys
import threading


import time
from flask import Flask, render_template, abort
# from turbo_flask import Turbo
import random
'''
app = Flask(__name__)
turbo = Turbo(app)


app.secret_key="dsl@iisc"
status=0
'''
import input_q
import error_handler
import platform
import reveal_globals
import dbcon
# import outer_join
import time
import copy
import from_clause
import db_minimizer
import error_handler
import initialization
import where_clause
import projection
import groupby_clause
import aggregation
import orderby_clause
import limit
import result_comparator
import executable
import correlated_samp
import view_minimizer
import copy_min
import nep
import aoa_pred
import cs2_impr


import psycopg2


import os.path




def extracted_part_info():
	print("inside:   reveal_proc_support.extracted_part_info")
	return {'SELECT':reveal_globals.global_select_op_proc.strip(),\
		  'FROM':reveal_globals.global_from_op.strip(),\
		  'WHERE':reveal_globals.global_where_op.strip(),\
		  'GROUP BY':reveal_globals.global_groupby_op.strip(),\
		  'ORDER BY':reveal_globals.global_orderby_op.strip(),\
		  'LIMIT': reveal_globals.global_limit_op.strip()}

def reveal_vp_start_gui():
    print("inside reveal.vp_start_gui")
    if 'windows' in str(platform.system()).lower():
        reveal_globals.global_os_name = 'windows'
    else:
        reveal_globals.global_os_name = 'linux'
    runreveal()
    # reveal_support_init()

def runreveal(*args):
    print("inside------reveal_support.runreveal")
    '''if reveal_globals.global_test_option == '':
        return'''
    if reveal_globals.global_input_type != "1":
        reveal_globals.global_input_type = "0"
    if reveal_globals.global_conn == None:
        if(not establishConnection()):
            return
    #CHECK FOR STORED PROCEDURE EXISTENCE AND ERROR HERE BY RUNNING ON SOME SAMPLE DATABASE
    #CLOSE THIS SCREEN AND CALL THE NEXT SCREEN
    reveal_globals.global_proc_prev_screen = "inp"
    extractionStart()
 
def getconn() :
    #change port 
    conn = psycopg2.connect(
   database=reveal_globals.database_in_use, user='postgres', password='root', host='localhost', port= '5432'
)
    return conn

'''
def getconn_gcloud() :
    conn=connector.connect(
        "abcd-356108:asia-south1:database",
        "pg8000",
        user="postgres",
        password="root",
        db="tpch"
    )
    return conn
'''

def establishConnection():
    print("inside------reveal_support.establishConnection")
    # reveal_globals.global_connection_string = str('0.0.0.0,5432,' + reveal_globals.global_db_instance + ',,,')
    # arg = reveal_globals.global_connection_string.split(',')
    reveal_globals.global_db_engine = 'PostgreSQL'
    conn=getconn()
    reveal_globals.global_conn = conn
    print("connected...")
    return True
   

def reveal_support_init():
    print("inside------reveal_support.init")   
    #INITIALIZE ALL CONCERNED GLOBAL/LOCAL VARIABLES
    # reveal_globals.query1=""
    reveal_globals.output1=""
    #error test
    # reveal_globals.error="No Error"


    reveal_globals.select_inp = ""
    reveal_globals.from_inp = ""
    reveal_globals.where_inp = ""
    reveal_globals.groupby_inp = ""
    reveal_globals.orderby_inp = ""
    reveal_globals.limit_inp = ""
    reveal_globals.global_input_type = ""

    reveal_globals.global_select_op = ""
    reveal_globals.global_select_op_proc = ""
    reveal_globals.global_from_op = ""
    reveal_globals.global_where_op = ""
    reveal_globals.global_groupby_op = ""
    reveal_globals.global_orderby_op = ""
    reveal_globals.global_limit_op = ""

    reveal_globals.global_clauses_with_syntactic_changes = ""
    reveal_globals.global_number_of_query_invocations = ""
    reveal_globals.global_tot_ext_time = ""

    reveal_globals.global_select_time = ""
    reveal_globals.global_min_time = ""
    reveal_globals.global_from_time = ""
    reveal_globals.global_where_time = ""
    reveal_globals.global_join_time = ""
    reveal_globals.global_filter_time = ""
    reveal_globals.global_groupby_time = ""
    reveal_globals.global_orderby_time = ""
    reveal_globals.global_agg_time = ""
    reveal_globals.global_limit_time = ""
    reveal_globals.global_assemble_time =""

    reveal_globals.global_conn = None

    reveal_globals.global_min_button = False
    reveal_globals.global_button_string = ""

    reveal_globals.global_min_instance_dict = {}
    reveal_globals.global_miniscule_instances_dict = {}

    reveal_globals.global_proc_prev_screen = ""
    reveal_globals.global_db_prev_screen = ""

    reveal_globals.global_no_execCall = 0

    reveal_globals.global_all_relations = []
    reveal_globals.global_pk_dict = {}
    reveal_globals.global_index_dict = {}

    reveal_globals.global_core_relations = []
    reveal_globals.global_join_graph = []
    reveal_globals.global_filter_predicates = []
    reveal_globals.global_projected_attributes = []
    reveal_globals.global_groupby_attributes = []
    reveal_globals.global_aggregated_attributes = []
    reveal_globals.global_orderby_attributes = []
    reveal_globals.global_limit = 1000

    reveal_globals.global_key_lists = []
    reveal_globals.global_output_list = []
    reveal_globals.global_projection_names = []
    reveal_globals.global_groupby_flag = False
    reveal_globals.global_attrib_types = []
    reveal_globals.global_all_attribs = []
    reveal_globals.global_key_attributes = []
    reveal_globals.global_d_plus_value = {}
    reveal_globals.global_attrib_max_length = {}
    reveal_globals.global_result_dict = {}
    reveal_globals.local_other_info_dict = {}
    reveal_globals.global_other_info_dict = {}
    reveal_globals.global_extracted_info_dict = {}

    reveal_globals.global_restore_flag = False

    reveal_globals.global_test_option = False


def extractionStart(*args):
	print("inside:   reveal_proc_support.extractionStart")
	func_from_start()


def func_from_start():
    print("inside:   reveal_proc_support.func_from_start")
    reveal_globals.local_start_time = time.time()
    reveal_globals.global_core_relations = from_clause.getCoreRelations() #aman
    print(reveal_globals.global_core_relations)
    temp = copy.deepcopy(reveal_globals.global_core_relations)
    if temp != [] and temp != False:
        reveal_globals.global_from_op = temp[0]
    else:
        return
    del temp[0]
    for elt in temp:
        reveal_globals.global_from_op = reveal_globals.global_from_op + ", " + elt
    func_from_Complete()

def func_from_Complete():
    print("inside:   reveal_proc_support.func_from_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_from_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time = 0
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['min'] = extracted_part_info()
    # update_load()
    func_min_start()


def func_min_start():
    # all_tables=[]
    # cur = reveal_globals.global_conn.cursor()
    # cur.execute("select table_name from information_schema.tables where table_schema ='public';")
    # temp=cur.fetchall()
    # cur.close()
    # for i in temp:
    #     reveal_globals.global_all_relations.append(i[0])
    dbcon.establishConnection()
    # for tabname in reveal_globals.global_core_relations:
    #     cur = reveal_globals.global_conn.cursor()
    #     cur.execute("DROP TABLE IF EXISTS " + tabname + "_restore;")
    #     cur.execute("Alter table " + tabname + " rename to " + tabname + "_restore;")
    #     cur.execute("create unlogged table " + tabname + " (like " + tabname + "_restore);")
    #     cur.execute("Insert into " + tabname + " select * from " + tabname + "_restore;")
    #     cur.close()
    print("inside:   reveal_proc_support.func_min_start")
    
	#INITIALIZATION
    if not (initialization.initialization()):
        exit(1)

    reveal_globals.local_start_time = time.time()
    if reveal_globals.mini_type == "kapil":
        if (db_minimizer.reduce_Database_Instance(reveal_globals.global_core_relations)):  #copy based minimizer
                func_min_Complete()
        else:
            reveal_globals.global_test_option = False
        
    else:
        
        x=time.time()
        if reveal_globals.correlated_sampling=="yes":
            cs2_impr.correlated_sampling_start()
            print("correlated sampling done!!!!!!")
        print("cs time====", time.time()-x)

        print("reveal_globals.minimizer=",reveal_globals.minimizer)
        if reveal_globals.minimizer=="copy_based":
            if (copy_min.reduce_Database_Instance(reveal_globals.global_core_relations)):  #copy based minimizer
                func_min_Complete()
            else:
                reveal_globals.global_test_option = False
        elif reveal_globals.minimizer=="view_based":
            if (view_minimizer.reduce_Database_Instance(reveal_globals.global_core_relations)):  #view based minimizer
                func_min_Complete()
            else:
                reveal_globals.global_test_option = False
    
   
        # if (db_minimizer.reduce_Database_Instance3(reveal_globals.global_core_relations)):  #view based minimizer
        #     func_min_Complete()
        # else:
        #     reveal_globals.global_test_option = False
        # if (view_minimizer.reduce_Database_Instance(reveal_globals.global_core_relations)):  #view based minimizer
        #     func_min_Complete()
        # else:
        #     reveal_globals.global_test_option = False

   
    # if (db_minimizer.reduce_Database_Instance3(reveal_globals.global_core_relations)):  
    # else:
    #     reveal_globals.global_test_option = False
        # goToInitScreen()

def func_min_Complete():
    print("inside:   reveal_proc_support.func_min_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_min_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    print("Minimization time ",reveal_globals.global_min_time)
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['join'] = extracted_part_info()
    # update_load()
    func_join_start()

def func_join_Complete():
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_join_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    print("inside:   reveal_proc_support.func_join_Complete")
    reveal_globals.global_extracted_info_dict['filter'] = extracted_part_info()
    # update_load()
    func_filter_start()

def func_join_start():
	print("inside:   reveal_proc_support.func_join_start")
	reveal_globals.local_start_time = time.time()
	where_clause.get_join_graph() #Returns JOIN GRAPH in Adjacency List format
	first_occur = True
	for elt in reveal_globals.global_join_graph:
		for i in range(1, len(elt)):
			if first_occur == True:
				reveal_globals.global_where_op = elt[0] + ' = ' + elt[i]
				first_occur = False
			else:
				reveal_globals.global_where_op = reveal_globals.global_where_op + ' and ' + elt[0] + ' = ' + elt[i]
	func_join_Complete()
	
def func_assemble_Complete():
    print("inside:   reveal_proc_support.func_assemble_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_assemble_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_select_op = reveal_globals.global_select_op.replace('as l_orderkey', '')	
    # print("end")
    # print("$$$$****$$$$")
    #time.sleep(50)
    # update_load()
    error_handler.restore_database_instance()

def func_assemble_start():
    print("inside:   reveal_proc_support.func_assemble_start")
    output=""
    reveal_globals.local_start_time = time.time()
    if reveal_globals.global_db_engine == 'PostgreSQL':
        output = "Select " +reveal_globals.global_select_op + "\n" + "From "  +reveal_globals.global_from_op
    if reveal_globals.global_where_op != '':
        output = output + "\n" + "Where " + reveal_globals.global_where_op
    if reveal_globals.global_groupby_op != '':
        output = output + "\n" + "Group By " + reveal_globals.global_groupby_op
    if reveal_globals.global_orderby_op != '':
        output = output + "\n" + "Order By " + reveal_globals.global_orderby_op
    if reveal_globals.global_limit_op  != '':
        output = output + "\n" + "Limit " + reveal_globals.global_limit_op 
    output = output + ";"
    # output = "Select " + reveal_globals.global_select_op + "\n" + "From "  + reveal_globals.global_from_op + "\n" + "Where " + reveal_globals.global_where_op + "\n" + "Group By "+ reveal_globals.global_groupby_op + "\n" + "Order By " + reveal_globals.global_orderby_op + "\n" + "Limit " + reveal_globals.global_limit_op + ";"
    print('EXTRACTED OUTPUT QUERY :')
    reveal_globals.output1=output
    print(reveal_globals.output1)
    func_assemble_Complete()  #changes made here0

#### start----  additions for nep
# def extractedQ():
# 	query = "Select " + reveal_globals.global_select_op_proc + "\n" + "From "  + reveal_globals.global_from_op
# 	if reveal_globals.global_where_op.strip() != '':
# 		query = query + "\n" + "Where " + reveal_globals.global_where_op
# 	if reveal_globals.global_groupby_op.strip() != '':
# 		query = query + "\n" + "Group By " + reveal_globals.global_groupby_op
# 	if reveal_globals.global_orderby_op.strip() != '':
# 		query = query + "\n" + "Order By " + reveal_globals.global_orderby_op
# 	if reveal_globals.global_limit_op.strip() != '':
# 		query = query + "\n" + "Limit " + reveal_globals.global_limit_op 
# 	query = query + ";"
# 	return query	

# def func_nep_start():
#     global w, root
#     Q_E = extractedQ()
#     reveal_globals.local_start_time = time.time()
	
# 	# Q_E_ = minimizer(reveal_globals.global_core_relations, Q_E)
#     #sneha
#     # Q_E_ = final_nep.sneha_nep_db_minimizer(reveal_globals.global_core_relations, Q_E)
#     Q_E_ = nep.nep_algorithm(reveal_globals.global_core_relations, Q_E)
#     print("Query with NEP", Q_E_)
#     func_nep_Complete()

# def func_nep_Complete():
# 	global w, root
	
# 	reveal_globals.local_end_time = time.time()
# 	reveal_globals.global_nep_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
# 	reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
	
# 	func_assemble_start()

##### end --- additions for nep

def func_limit_Complete():
    print("inside:   reveal_proc_support.func_limit_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_limit_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    func_assemble_start()

    # update_load()
    # func_nep_start()

def func_limit_start():
	print("inside:   reveal_proc_support.func_limit_start")
	reveal_globals.local_start_time = time.time()
	reveal_globals.global_limit = limit.get_limit()
	if reveal_globals.global_limit is not None:
		reveal_globals.global_limit_op = str(reveal_globals.global_limit)
	func_limit_Complete()


def func_orderby_Complete():
    print("inside:   reveal_proc_support.func_orderby_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_orderby_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['limit'] = extracted_part_info()
    # update_load()
    func_limit_start()             

def func_orderby_start():
	print("inside:   reveal_proc_support.func_orderby_start")
	reveal_globals.local_start_time = time.time()
	reveal_globals.global_orderby_attributes = orderby_clause.get_orderby_attributes()
	first_occur = True
	for elt in reveal_globals.global_orderby_attributes:
		if first_occur == True:
			reveal_globals.global_orderby_op = reveal_globals.global_output_list[elt[0].index] + ' ' + elt[1]
			first_occur = False
		else:
			reveal_globals.global_orderby_op = reveal_globals.global_orderby_op + ', ' + reveal_globals.global_output_list[elt[0].index] + ' ' + elt[1]
	func_orderby_Complete()


def func_agg_Complete():
    print("inside:   reveal_proc_support.func_agg_Complete")
    reveal_globals.global_select_op_proc = reveal_globals.global_select_op
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_agg_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['order by'] = extracted_part_info()
    # update_load()
    func_orderby_start()

def func_agg_start():
    print("inside:   reveal_proc_support.func_agg_start")
    reveal_globals.local_start_time = time.time()
    reveal_globals.global_aggregated_attributes = aggregation.get_aggregation()
    refine_Query()   
    func_agg_Complete()


def refine_Query():
	print("inside:   reveal_proc_support.refine_Query")
	for i in range(len(reveal_globals.global_projected_attributes)):
		attrib = reveal_globals.global_projected_attributes[i]
		if attrib in reveal_globals.global_key_attributes and attrib in reveal_globals.global_groupby_attributes:
			if not ('sum' in reveal_globals.global_aggregated_attributes[i][1] or 'count' in reveal_globals.global_aggregated_attributes[i][1]):
				reveal_globals.global_aggregated_attributes[i] = (reveal_globals.global_aggregated_attributes[i][0], '')
	temp_list = copy.deepcopy(reveal_globals.global_groupby_attributes)
	for attrib in temp_list:
		if attrib not in reveal_globals.global_projected_attributes:
			try:
				reveal_globals.global_groupby_attributes.remove(attrib)
			except:
				pass
			continue
		remove_flag = True
		for elt in reveal_globals.global_aggregated_attributes:
			if elt[0] == attrib and (not ('sum' in elt[1] or 'count' in elt[1])):
				remove_flag = False
				break
		if remove_flag == True:
			try:
				reveal_globals.global_groupby_attributes.remove(attrib)
			except:
				pass
	#UPDATE OUTPUTS
	first_occur = True
	reveal_globals.global_groupby_op = ''
	for i in range(len(reveal_globals.global_groupby_attributes)):
		elt = reveal_globals.global_groupby_attributes[i]
		if first_occur == True:
			reveal_globals.global_groupby_op = elt
			first_occur = False
		else:
			reveal_globals.global_groupby_op = reveal_globals.global_groupby_op + ", " + elt
	first_occur = True
	for i in range(len(reveal_globals.global_projected_attributes)):
		elt = reveal_globals.global_projected_attributes[i]
		reveal_globals.global_output_list.append(copy.deepcopy(elt))
		if reveal_globals.global_aggregated_attributes[i][1] != '':
			elt = reveal_globals.global_aggregated_attributes[i][1] + '(' + elt + ')'
			if 'count' in reveal_globals.global_aggregated_attributes[i][1]:
				elt = reveal_globals.global_aggregated_attributes[i][1]
			reveal_globals.global_output_list[-1] = copy.deepcopy(elt)
		if elt != reveal_globals.global_projection_names[i] and reveal_globals.global_projection_names[i] != '':
			elt = elt + ' as ' + reveal_globals.global_projection_names[i]
			reveal_globals.global_output_list[-1] = copy.deepcopy(reveal_globals.global_projection_names[i])
		if first_occur == True:
			reveal_globals.global_select_op = elt
			first_occur = False
		else:
			reveal_globals.global_select_op = reveal_globals.global_select_op + ", " + elt	
	return

def func_groupby_Complete():
    print("inside:   reveal_proc_support.func_groupby_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_groupby_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['agg'] = extracted_part_info()
    # update_load()
    func_agg_start()


def func_groupby_start():
    print("inside:   reveal_proc_support.func_groupby_start")
    reveal_globals.local_start_time = time.time()
    first_occur = True
    reveal_globals.global_groupby_attributes, reveal_globals.global_groupby_flag = groupby_clause.getGroupByAttributes()
    for i in range(len(reveal_globals.global_groupby_attributes)):
        elt = reveal_globals.global_groupby_attributes[i]
        if first_occur == True:
            reveal_globals.global_groupby_op = elt
            first_occur = False
        else:
            reveal_globals.global_groupby_op = reveal_globals.global_groupby_op + ", " + elt
    func_groupby_Complete()


def func_project_Complete():
    print("inside:   reveal_proc_support.func_project_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_projection_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['group by'] = extracted_part_info()
    # update_load()
    func_groupby_start()

def func_project_start():
	print("inside:   reveal_proc_support.func_project_start")
	reveal_globals.local_start_time = time.time()
	reveal_globals.global_projected_attributes, reveal_globals.global_projection_names = projection.getProjectedAttributes()
	first_occur = True
	for i in range(len(reveal_globals.global_projected_attributes)):
		elt = reveal_globals.global_projected_attributes[i]
		reveal_globals.global_output_list.append(copy.deepcopy(elt))
		if elt != reveal_globals.global_projection_names[i] and reveal_globals.global_projection_names[i] != '':
			elt = elt + ' as ' + reveal_globals.global_projection_names[i]
			reveal_globals.global_output_list[-1] = copy.deepcopy(reveal_globals.global_projection_names[i])
		if first_occur == True:
			reveal_globals.global_select_op_proc = elt
			first_occur = False
		else:
			reveal_globals.global_select_op_proc = reveal_globals.global_select_op_proc + ", " + elt
	func_project_Complete()

################## start-- additions for aoa_pred
# def func_aoa_Complete():

# 	#---todo---
# 	# reveal_globals.global_where_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
# 	# reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
# 	# reveal_globals.global_extracted_info_dict['projection'] = extracted_part_info()

# 	func_project_start()

# def func_aoa_start():
	
# 	# reveal_globals.local_start_time = time.time() #aman
# 	reveal_globals.global_filter_predicates = aoa_pred.extract_aoa() #referenced aoa_pred.extract_aoa
# 	# print("AoA pred time: ", time.time() - reveal_globals.local_start_time) #aman
# 	# print(reveal_globals.global_filter_aoa)
# 	func_aoa_Complete()


################## end-- additions for aoa_pred

def func_filter_Complete():
    print("inside:   reveal_proc_support.func_filter_Complete")
    reveal_globals.local_end_time = time.time()
    reveal_globals.global_filter_time = str(round(reveal_globals.local_end_time - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time += reveal_globals.local_end_time - reveal_globals.local_start_time
    reveal_globals.global_extracted_info_dict['projection'] = extracted_part_info()
    # update_load()
    func_project_start()
    # func_aoa_start()


def func_filter_start():
    # print("inside:   reveal_proc_support.func_filter_start")
    reveal_globals.local_start_time = time.time() #aman
    reveal_globals.global_filter_predicates = where_clause.get_filter_predicates()
    # print("where time: ", time.time() - reveal_globals.local_start_time) #aman
    for elt in reveal_globals.global_filter_predicates:
        predicate = ''
        if elt[2].strip() == 'range': 
            if "<class 'datetime.date'>"==str(type(elt[4])): #make changes for date in here
                predicate = elt[1] + " between date"  + " '" + str(elt[3]) + "'" + " and date" + " '" + str(elt[4]) + "'"
            # print(type(elt[4]))
            elif '-' in str(elt[4]):
                predicate = elt[1] + " between "  + str(elt[3]) + " and " + str(elt[4])
            else:
                predicate = elt[1] + " between "  + " '" + str(elt[3]) + "'" + " and " + " '" + str(elt[4]) + "'"
        elif elt[2].strip() == '>=':
            if '-' in str(elt[3]):
                predicate = elt[1] + " " + str(elt[2]) + " '" + str(elt[3]) + "' "
            else:
                predicate = elt[1] + " " + str(elt[2]) + " " + str(elt[3])
        elif 'equal' in elt[2] or 'like' in elt[2].lower() or '-' in str(elt[4]):
            predicate = elt[1] + " " + str(elt[2]).replace('equal', '=') + " '" + str(elt[4]) + "'"
        else:
            predicate = elt[1] + ' ' + str(elt[2]) + ' ' + str(elt[4])
        if reveal_globals.global_where_op == '':
            reveal_globals.global_where_op = predicate
        else:
            reveal_globals.global_where_op = reveal_globals.global_where_op + " and " + predicate
    func_filter_Complete()

def hash_result_comparator():
    dbcon.establishConnection()
    extracted_query=reveal_globals.output1
    # res= executable.getExecOutput()
    reveal_globals.local_start_time = time.time()
    #call hash based result comparator
    a=result_comparator.match(extracted_query)
    reveal_globals.global_hashres_time = str(round(time.time() - reveal_globals.local_start_time, 1)) + "      sec"
    reveal_globals.global_tot_ext_time +=round(time.time() - reveal_globals.local_start_time, 1)
    # error_handler.restore_database_instance()
    if(a):
        print(" results Same")
    else:
        print("results different")
    #     return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"],res_comp="Comparison Successful!!\n \n Output tables of Extracted Query and Hidden Query are Same.")
    # else:
    #     return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"],res_comp="Comparison Unsuccessful!!\n \n Output tables of Extracted Query and Hidden Query are Different.")



'''
if __name__ == '__main__':
    reveal_vp_start_gui()
 
 '''

'''
@app.route("/")
def session_page():
    reveal_support_init()
    dbcon.establishConnection()
    return render_template('page1.html')

@app.route("/query_input_page",methods=['POST','GET'])
def query_input_page():
    # if(request.method=="POST"):
    #     # session["name"]=n     #session is stored in form of doctionary
    #     session["i_query"]=[]
    #     session["o_query"]=[]
    # else:
    #     pass
    #     # n=request.form.get("uname")
    reveal_support_init()
    dbcon.establishConnection()
    return render_template('page1.html',er=reveal_globals.error,q=reveal_globals.query1)



    
@app.route("/query_process_page",methods=['POST','GET'])
def query_process_page():
    # try:
    if request.method=="POST":
        reveal_globals.error=""
        reveal_globals.query1=""
        q=request.form.get("QUERY")
        reveal_globals.minimizer=request.form.get("minimizer")
        # print("minimizer====",reveal_globals.minimizer)
        reveal_globals.correlated_sampling=request.form.get("correlated_sampling")
        
        reveal_globals.query1=q
        print("point-1")
        reveal_vp_start_gui()
        print("point-2")
        op=reveal_globals.output1
        session["i_query"]=reveal_globals.query1
        session["o_query"]=op
        print("Error:  ",reveal_globals.error)
        if(reveal_globals.error==""):
            return redirect('/query_output_page')
        else:
            return redirect('/query_input_page')
    # except:
    #     return render_template('error.html',er=reveal_globals.error)







# OLd query_process_page()
# @app.route("/query_process_page",methods=['POST','GET'])
# def query_process_page():
#     if request.method=="POST":
#         q=request.form.get("QUERY")
#         reveal_globals.query1=q
#         reveal_vp_start_gui()
#         op=reveal_globals.output1
#         session["i_query"]=reveal_globals.query1
#         session["o_query"]=op
#         update_load()
#         # return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"])
#         return redirect('/query_output_page')
#     else:
#         return redirect("/query_input_page")




@app.route("/query_output_page")
def query_output_page():
 
    x="Used correlated sampling : "+reveal_globals.correlated_sampling+ " and Used "+reveal_globals.minimizer+" minimizer " 
    return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"], min_combination=x)
    # return render_template('page2.html',output_query=op,input_query=ip)


@app.route("/back_to_query_page")
def back_to_query_page():
    error_handler.restore_database_instance
    reveal_support_init()
    return redirect("/query_input_page")


# @app.route("/set_view_based_minimizer")
# def set_view_based_minimizer():
#     print(" inside set_view_based_minimizer")
#     reveal_globals.view_based_minimizer=True
#     reveal_globals.correlated_sampling=False
#     reveal_globals.copy_based_minimizer= False
#     return render_template('page1.html',min_option="Note: Using View Based Minimizer")


# @app.route("/set_copy_based_minimizer")
# def set_copy_based_minimizer():
#     print("set_copy_based_minimizer")
#     reveal_globals.view_based_minimizer=False
#     reveal_globals.correlated_sampling=False
#     reveal_globals.copy_based_minimizer= True
#     return render_template('page1.html',min_option="Note: Using Copy Based Minimizer")

# #CORRELATED SAMPLING
# @app.route("/set_correlated_sampling")
# def set_correlated_sampling():
#     print("set_correlated_sampling")
#     reveal_globals.correlated_sampling=True
#     reveal_globals.view_based_minimizer=True
#     reveal_globals.copy_based_minimizer= False
#     return render_template('page1.html',min_option="Note: Using Correlated Sampling")




@app.route("/hash_result_comparator")
def hash_result_comparator():
    dbcon.establishConnection()
    extracted_query=reveal_globals.output1
    res= executable.getExecOutput()
    #call hash based result comparator
    a=result_comparator.match(extracted_query,res)
    error_handler.restore_database_instance()
    if(a):
        return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"],res_comp="Comparison Successful!!\n \n Output tables of Extracted Query and Hidden Query are Same.")
    else:
        return render_template('page2.html',output_query=session["o_query"],input_query=session["i_query"],res_comp="Comparison Unsuccessful!!\n \n Output tables of Extracted Query and Hidden Query are Different.")







# def update_load():
#     with app.app_context():
#         turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))


@app.context_processor
def inject_load():
    return {
    'from_time':reveal_globals.global_from_time,
    'minimization_time': reveal_globals.global_min_time,
    'select_time':reveal_globals.global_select_time,
    'where_time':reveal_globals.global_where_time,
    'join_time':reveal_globals.global_join_time,
    'filter_time':reveal_globals.global_filter_time,
    'groupby_time':reveal_globals.global_groupby_time, 
    'orderby_time':reveal_globals.global_orderby_time,
    'agg_time':reveal_globals.global_agg_time,
    'limit_time':reveal_globals.global_limit_time,
    'assemble_time':reveal_globals.global_assemble_time,
    'from_op':reveal_globals.global_from_op,
    'select_op':reveal_globals.global_select_op,
    'where_op':reveal_globals.global_where_op,
    'groupby_op':reveal_globals.global_groupby_op,
    'orderby_op':reveal_globals.global_orderby_op,
    'limit_op':reveal_globals.global_limit_op,
    }


if __name__=='__main__':
    # app.run(host='0.0.0.0', port=8090, debug=True)
    app.run(host='127.0.0.1', port=8083)
    #change while web deloyment

'''





reveal_support_init()
dbcon.establishConnection()


reveal_globals.mini_type = "kapil"
# print("minimizer====",reveal_globals.minimizer)
#level-1
reveal_globals.correlated_sampling="yes"
# reveal_globals.correlated_sampling="no"

#level-2      
# reveal_globals.minimizer="copy_based"
reveal_globals.minimizer="view_based"
  
  
input_q.get_input_query()
reveal_vp_start_gui()

# op=reveal_globals.output1
# print(op)
# print("Error:  ", reveal_globals.error)
x="Used correlated sampling : " + reveal_globals.correlated_sampling + " and Used " + reveal_globals.minimizer + " minimizer " 
print(x) 

# error_handler.restore_database_instance()
# reveal_support_init()
# hash_result_comparator()

print("From Clause Time          : ", reveal_globals.global_from_time)
print("total DB Minimizer Time   : ", reveal_globals.global_min_time)
print("---copy_min_time          : ", reveal_globals.copy_min_time)
print("---view_min_time          : ", reveal_globals.view_min_time)
print("---cs_time s              : ", reveal_globals.cs_time)
print("Join Clause Extr          : ", reveal_globals.global_join_time)
print("Filter Predicate Ext      : ", reveal_globals.global_filter_time)
print("Projection extractor      : ", reveal_globals.global_projection_time)
print("Group By                  : ", reveal_globals.global_groupby_time)
print("Aggregate Time            : ", reveal_globals.global_agg_time)
print("Order By                  : ", reveal_globals.global_orderby_time)
print("Limit                     : ", reveal_globals.global_limit_time)
# print("Hash result comparator    : ", reveal_globals.global_hashres_time)
print("total extraction time     : ", reveal_globals.global_tot_ext_time)

# hash_result_comparator()
# print("Hash result comparator                           : ", reveal_globals.global_hashres_time)
# print("total extraction time + hash comparison time     : ", reveal_globals.global_tot_ext_time)