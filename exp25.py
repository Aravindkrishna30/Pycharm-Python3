from numpy import *
arr1=array([1,2,35,3,2,33,32])
arr2=arr1.copy() #deep copy
#arr2=arr1.view() #shallow copy
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

