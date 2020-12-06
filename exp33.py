def person(name, **data):
    print(name)
    #print(data)

    for i,j in data.items():
        print(i,j)

person('Aravind',age=20, city='chennai', mobileno=87779)
#keyworded variable length Arguments