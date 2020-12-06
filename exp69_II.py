import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Krish@301298")
print(mydb)

if(mydb):
    print("Connection successful")
else:
    print("Connection unsuccessful")