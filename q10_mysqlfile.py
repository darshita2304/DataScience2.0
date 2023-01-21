## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q10: create a class to do a bulk upload a file in mysql - csv or text file

import mysql.connector
import logging
import panda as pd

logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q10_mysqlfile:
    
    def __init__(self, host, username, password, ):
        logging.info("this is connection intitial fn")
        try:
            self.conn =  mysql.connector.connect(host=host, user=username,password=password)
            self.cur = self.conn.cursor()
            logging.info("connection sucessful")

            #self.cur.execute("create database studentsdb")
            self.cur.execute("use studentsdb")
            logging.info("students db is in use...")

        except Exception as e:
            logging.error("there is some issue with conncetion with mysql")
            logging.error(e)

    def insertfromcsv(self, csvfile):
        csvdata = pd.read_csv(csvfile, index_col=False)
        df = pd.DataFrame(data)

        try:
            logging.info("drop table if already exists")
            self.cur.execute("DROP TABLE IF EXISTS test")

            sql = '''CREATE TABLE test(
            symbol varchar(20) NOT NULL,
            token int NOT NULL,
            name varchar(50) NOT NULL,
            lotsize DECIMAL(2,1),
            exch_seg CHAR(11) NOT NULL,
            tick_size int
            )'''
            # Creating a table
            self.cur.execute(sql)
            logging.info("creating new table")
            
            for row in df.itertuples():
                self.cur.execute('''
                INSERT INTO products (symbol, token, name, lotsize, exch_seg, tick_size)
                VALUES (?,?,?,?,?,?)
                ''',
                row.symbol, 
                row.token,
                row.name,
                row.lotsize,
                row.exch_seg,
                row.tick_size
                )
            
            logging.info("inserted record...")
            print('record inserted sucessfully...')
            self.conn.commit()
            return 
            
        except Exception as e:
            logging.error("there is some issue with conncetion with mysql")
            logging.error(e)

obj = q10_mysqlfile("localhost",'abc','password')
obj.insertfromcsv('test.csv')


