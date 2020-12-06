#Linear search
pos = -1
def search(list,n):
    i = 0
    for i in list:
        if i == n:
    #while i<len(list):
        #if list[i] == n:
            globals()['pos'] = i
            return True;
        #i+=1
    return False;

list=[3,4,5,6,9,8]
n = int(input("Enter the Value to search in the List :  "))

if search(list,n):
    print("Status : Found"," || Position : ", pos+1)
else:
    print("Not Found")

print("Thank you for using our Services, Bye !!!")