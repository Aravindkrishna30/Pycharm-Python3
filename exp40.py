
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

a=fact(int(input("Enter the number : ")))
print("result=",a )
print("Thank you for using our serivice.")
print("Bye!!!")