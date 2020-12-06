# pass List to a function

def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even , odd
#lst=[20,23,24,12,21,22,11,14]
#lst=input('Enter the value: ') #wrong
# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
lst = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", lst)
#to restrict to don't exist the count
i=1
while i<=n:
   break
   i+=1

even,odd=count(lst)
#print(odd)
#print(even)
print('Even :{} and Odd : {}'.format(even,odd))
