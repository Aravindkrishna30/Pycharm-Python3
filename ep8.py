#break
avg = 5
x=int(input('Enter the no of candies you want : '))
i=1
while i<=x:
    if i>avg:
        print("out of stock")
        break
    print("Candy")
    i+=1
print("Bye!!!")