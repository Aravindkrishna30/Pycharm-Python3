#cpy the img from one file to another
f=open('Img_111.jpg','rb')

f1=open('exp64_desty.JPG', 'wb')

for i in f:
    # print(i)
    f1.write(i)
