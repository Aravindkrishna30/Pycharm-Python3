from array import *
arr=array('i',[])
n=int(input("Enter the size of the array: "))
for i in range(n):
    x=int(input("Enter the values of the Array: "))
    arr.append(x)
print(arr)

val= int(input("Enter the values to search "))
k=0
for j in arr:
    if j==val:
        print(k)
        break
    k+=1
print(arr.index(val))


print("Thank You for Visting!!!")
