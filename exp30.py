#37-33
def update(lst):
    print("x =", id(lst))
    lst[1]=25
    print(id(lst))
    print("x =", lst)

lst=[10,20,30,28]
print(id(lst))
update(lst)
print("lst =", lst)