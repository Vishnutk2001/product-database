import sqlite3

connection = sqlite3.connect("product.db")

# connection.execute(''' CREATE TABLE PRODUCTDATA(
#                         CODE INTEGER PRIMARY KEY AUTOINCREMENT,
#                         NAME TEXT,
#                         PRICE INTEGER,
#                         DISTRIBUTORNAME TEXT,
#                         MANNAME TEXT
#
# );   ''')
# print("table created successfully")

getCode = input("enter code : ")
getName = input("enter name : ")
getprice = input("enter price : ")
getdistributorname = input("enter distributorname : ")
getmanname = input("enter manname : ")
connection.execute("INSERT INTO PRODUCTDATA(CODE,NAME,PRICE,DISTRIBUTORNAME,MANNAME)\
VALUES("+getCode+",'"+getName+"',"+getprice+",'"+getdistributorname+"','"+getmanname+"')")
connection.commit()
connection.close()
print("INSERTED SUCCESSFULLY")
