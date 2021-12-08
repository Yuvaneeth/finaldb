import pymysql
import psycopg2
from time import time
import pyodbc
import pprint
import json
import warnings


class connect_mysql():
    def __init__(self, host="localhost", user="myuser", password=None, db="db"):
        self.db = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cursor = self.db.cursor()

    def run_query(self, query_statement):
        start_time = int(round(time() * 1000))
        self.cursor.execute(query_statement)
        col_info = self.cursor.description
        result = self.cursor.fetchall()
        print(result)
        query_time = str(int(round(time() * 1000)) - start_time) + " ms"
        # if len(result) > 1000:
        #     result = result[:99]
        #     query_time += '\nThe result is too larger to transmit and display, so we limit the size to return'
        col_name = []
        for i in range(len(col_info)):
            col_name.append(col_info[i][0])
        return col_name, result, query_time



    def disconnect(self):
        # print(self.cursor)
        self.cursor.close()
        self.db.close()



class connect_redshift():
    def __init__(self, host="localhost", database='database', user='awsuser', password='Cs123456', port=5439):
        self.con = psycopg2.connect(host=host, dbname=database, port=port, password=password, user=user)
        self.cur = self.con.cursor()

    def run_query(self, query_statement):
        start_time = int(round(time() * 1000))
        self.cur.execute(query_statement)
        col_info = self.cur.description
        result = self.cur.fetchall()
        query_time = str(int(round(time() * 1000)) - start_time) + " ms"
        # if len(result) > 1000:
        #     result = result[:99]
        #     query_time += '\nThe result is too larger to transmit and display, so we limit the size to return'
        col_name = []
        for i in range(len(col_info)):
            col_name.append(col_info[i][0])
        return col_name, result, query_time
    
    def disconnect(self):
        self.cur.close()
        self.con.close()



class connect_mongodb():
    def __init__(self,driver,server,database,port,user,password):
    # def __init__(self):
        # pyodbc.connect('Driver={MongoDB ODBC Driver};'
        #               'Server=server_name;'
        #               'Database=database_name;'
        #               'Trusted_Connection=yes;',autocommit=True)
        # driver="{"+driver+"}"
        self.db=pyodbc.connect('DRIVER='+driver+';Server='+server+';Port='+port+';Database='+database+';user='+user+';password='+password+'',autocommit=True)
        # cnxn = pyodbc.connect('DRIVER={MongoDB ODBC Driver};Server=127.0.0.1;Port=3307;User=neel;Password=mongo123;Database=ADNI', autocommit=True)
        # self.db = pyodbc.connect('DRIVER={MongoDB Unicode ODBC 1.4.2};Server=18.219.52.254;Port=3307;User=neel;Password=mongo123', autocommit=True)
        self.cursor = self.db.cursor()

    def run_query(self, query_statement):
        start_time = int(round(time() * 1000))
        # self.cursor.execute("use ADNI;")

        self.cursor.execute(query_statement)
        col_info = self.cursor.description
        result = self.cursor.fetchall()
        print(result)
        query_time = str(int(round(time() * 1000)) - start_time) + " ms"
        # if len(result) > 1000:
        #     result = result[:99]
        #     query_time += '\nThe result is too larger to transmit and display, so we limit the size to return'
        col_name = []
        for i in range(len(col_info)):
            col_name.append(col_info[i][0])
        return col_name, result, query_time


    def disconnect(self):
        self.cursor.close()
        self.db.close()





# class connect_mongodb():
#     def __init__(self, host="localhost", user="myuser", password=None, db="db"):
#         self.db = pymysql.connect(host=host, user=user, password=password, db=db)
#         self.cursor = self.db.cursor()

#     def run_query(self, query_statement):
#         start_time = int(round(time() * 1000))
#         self.cursor.execute(query_statement)
#         col_info = self.cursor.description
#         result = self.cursor.fetchall()
#         print(result)
#         query_time = str(int(round(time() * 1000)) - start_time) + " ms"
#         # if len(result) > 1000:
#         #     result = result[:99]
#         #     query_time += '\nThe result is too larger to transmit and display, so we limit the size to return'
#         col_name = []
#         for i in range(len(col_info)):
#             col_name.append(col_info[i][0])
#         return col_name, result, query_time



#     def disconnect(self):
#         # print(self.cursor)
#         self.cursor.close()
#         self.db.close()


# class connect_mongo():
#     def __init__(self):
#         self.db = pyodbc.connect('DRIVER={MongoDB ODBC Driver};Server=0.0.0.0;Port=3307;User=neel;Password=mongo123', autocommit=True)
#         self.cursor = self.db.cursor()

#     def run_query(self, query_statement):
#         start_time = int(round(time() * 1000))
#         self.cursor.execute(query_statement)
#         col_info = self.cursor.description
#         result = self.cursor.fetchall()
#         print(result)
#         query_time = str(int(round(time() * 1000)) - start_time) + " ms"
#         # if len(result) > 1000:
#         #     result = result[:99]
#         #     query_time += '\nThe result is too larger to transmit and display, so we limit the size to return'
#         col_name = []
#         for i in range(len(col_info)):
#             col_name.append(col_info[i][0])
#         return col_name, result, query_time



    # def disconnect(self):
    #     # print(self.cursor)
    #     self.cursor.close()
#     #     self.db.close()
# if __name__=="__main__":
#     c=connect_mongodb()
#     c.run_query("use ADNI;")
