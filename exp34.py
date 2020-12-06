a=10
print(id(a))
def diff_variables():
   # global a
    a=9
    x=globals()['a']
    print(id(x))
    print('local=',a)
    globals()['a']=15

diff_variables()

print("outside=",a)