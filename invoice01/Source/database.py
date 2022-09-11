from msilib.schema import Error
from multiprocessing.connection import Connection
import mysql.connector
from mysql.connector import *
from data  import BDContext

##Connect to Database 
##Add data
try:
    data=BDContext()
    connection=mysql.connector.connect(host=data.host,user=data.user,password=data.password,database=data.database)
    cursor=connection.cursor()
    cursor.callproc("getUsers")
    for result in cursor.stored_results():
        print(result.fetchall())
    print("Stored procedure was executed")
except Error as a:
    print("",a)

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection is closed")

