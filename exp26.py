#35-31
from numpy import *
#arr=array([
#        [1,2,3,4,3,2],
#        [2,3,4,6,7,8]
#])
#print(arr)
#print(arr.dtype) #datatype
#print(arr.ndim) #dimentions
#print(arr.shape) # no of rows and colomns
#print(arr.size) # siz of the entire block

#arr1=arr.flatten() #single dim
#arr2=arr1.reshape(3,4) #Multi dim
#arr2=arr1.reshape(2,2,3) #3d
#print(arr2)
m1=matrix('1 2 3;4 6 7;6 4 3')
m2=matrix('7 8 9;6 7 5;5 4 3')
#m=m1+m2;
#print(m)
m=m1*m2;
print(m)
#print(diagonal(m))#diagonal value
#print(m.min())
#print(m.max())