import mysql.connector

def db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        #host='mysql_db',
        user='root',
        password='ejlc1999',
        database='challenge_api'
    )
    return connection