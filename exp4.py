#Add or Even
x=int(input('Enter the num:'))
r = x % 2

if(r==0):
    print('Number is Even')
    if(x>5):
        print("Num is Greater")
    else:
        print("Num is small")
        print("see u again!!")
else:
    print('Num is odd')
    if(x<10):
        print("Num is small")
    else:
        print("Num is greater")
print("Bye!!!")
