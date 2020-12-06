a=int(input("Enter the first number: "))
b=int(input("Enter the Second number: "))

try:
   print("Resource Open")
   print(a/b)
   #print("Resource Close")
   k=int(input("Enter a Number : "))
   print(k)

except ZeroDivisionError as e:
    print("Hey, you cannot divide a Number by Zero", "|| Error type =",e)
    #print("Resource Close")

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Something went Wrong....')

#print("bye")

#Finally block will be executed if we get error as well as if we don't get the error
finally:
    print("Resource Close")