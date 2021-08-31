 import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', database='cbtTest_db')

mycursor = mycon.cursor()

mycursor.execute("CREATE DATABASE cbtTest_db")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

mycursor.execute("CREATE TABLE customers (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")

mycursor.execute("SHOW TABLES")
for table in mycursor: 
    print(table)

mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")
mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone);")