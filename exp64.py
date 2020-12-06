#Read data
#f= open('exp64_MyData','r')
#print(f.read())
#print(f.readlines())
#print(f.readable())
#print(f.readline(), end="")

#Write data
#f1= open('exp64_Mywrite','w')
#f1.write("Something new to the file")
#f1.write('\n People')

#Append Data
#f1= open('exp64_Mywrite','a')
#f1.write("DELL Laptop -> Is is the coolest one....!")

#Read all data from "exp4=64_Mywrite" then write into "exp64_MyData"

f = open('exp64_Mywrite','r')
f1=open('exp64_MyData', 'w')

for data in f:
  f1.write(data)

