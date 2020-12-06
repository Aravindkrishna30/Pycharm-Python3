import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="Aravind", passwd="Krish@301298")
mycusor = mydb.cursor()
#mycusor.execute("select version()")
mycusor.execute("select * from student")
result = mycusor.fetchone()
#print("Database version; %s"% data)
for i in mycusor:
    print(i)
#mydb.close()