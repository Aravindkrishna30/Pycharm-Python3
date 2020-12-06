#37-33
def update(x):
    print("x =", id(x))
    x=8
    print("x8 =", id(x))
    print("x =", x)

a=10
print("a =", id(a))
update(10) #pass a value
print("a =", a)