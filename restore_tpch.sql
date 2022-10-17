BEGIN;
	CREATE TABLE PART ( P_PARTKEY INTEGER , P_NAME VARCHAR(55), P_MFGR CHAR(25), P_BRAND CHAR(10), P_TYPE VARCHAR(25), P_SIZE INTEGER, P_CONTAINER CHAR(10), P_RETAILPRICE DECIMAL, P_COMMENT VARCHAR(23) );
	copy PART FROM '/services/app/part.csv'  WITH (FORMAT csv, DELIMITER '|');
COMMIT;

BEGIN;

	CREATE TABLE REGION ( R_REGIONKEY INTEGER , R_NAME CHAR(25), R_COMMENT VARCHAR(152) );
	COPY region FROM '/services/app/region.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;

BEGIN;
	CREATE TABLE NATION ( N_NATIONKEY INTEGER , N_NAME CHAR(25), N_REGIONKEY BIGINT , N_COMMENT VARCHAR(152) );

	COPY nation FROM '/services/app/nation.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;  

BEGIN;

	CREATE TABLE SUPPLIER ( S_SUPPKEY INTEGER , S_NAME CHAR(25), S_ADDRESS VARCHAR(40), S_NATIONKEY BIGINT , S_PHONE CHAR(15), S_ACCTBAL DECIMAL, S_COMMENT VARCHAR(101) );
	COPY supplier FROM 'services/app/supplier.csv' WITH (FORMAT csv, DELIMITER '|');
	

COMMIT;

BEGIN;

	CREATE TABLE CUSTOMER ( C_CUSTKEY INTEGER , C_NAME VARCHAR(25), C_ADDRESS VARCHAR(40), C_NATIONKEY BIGINT , C_PHONE CHAR(15), C_ACCTBAL DECIMAL, C_MKTSEGMENT CHAR(10), C_COMMENT VARCHAR(117) );

	COPY customer FROM '/services/app/customer.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;

BEGIN;

	CREATE TABLE PARTSUPP ( PS_PARTKEY BIGINT , PS_SUPPKEY BIGINT , PS_AVAILQTY INTEGER, PS_SUPPLYCOST DECIMAL, PS_COMMENT VARCHAR(199) );
	COPY partsupp FROM '/services/app/partsupp.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;



BEGIN;
CREATE TABLE ORDERS ( O_ORDERKEY INTEGER , O_CUSTKEY BIGINT , O_ORDERSTATUS CHAR(1), O_TOTALPRICE DECIMAL, O_ORDERDATE DATE, O_ORDERPRIORITY CHAR(15), O_CLERK CHAR(15), O_SHIPPRIORITY INTEGER, O_COMMENT VARCHAR(79) );
	COPY orders FROM '/services/app/orders.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;



BEGIN;

CREATE TABLE LINEITEM ( L_ORDERKEY BIGINT , L_PARTKEY BIGINT , L_SUPPKEY BIGINT , L_LINENUMBER INTEGER, L_QUANTITY DECIMAL, L_EXTENDEDPRICE DECIMAL, L_DISCOUNT DECIMAL, L_TAX DECIMAL, L_RETURNFLAG CHAR(1), L_LINESTATUS CHAR(1), L_SHIPDATE DATE, L_COMMITDATE DATE, L_RECEIPTDATE DATE, L_SHIPINSTRUCT CHAR(25), L_SHIPMODE CHAR(10), L_COMMENT VARCHAR(44) );

	COPY lineitem FROM '/services/app/lineitem.csv' WITH (FORMAT csv, DELIMITER '|');

COMMIT;

