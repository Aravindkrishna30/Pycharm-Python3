from functools import reduce
#def is_even(n):
#    return n%2==0
#def update(n):
#   return n*2
#def add_all(a,b):
#    return a+b

nums =[1,2,3,4,56,7,8,4]
evens=list(filter(lambda n :n%2==0,nums))
print(evens)
doubles=list(map(lambda n : n*2,evens))
print(doubles)
sum=reduce(lambda a,b : a+b,doubles)
print(sum)