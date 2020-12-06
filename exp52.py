 #inside class     -> 58/#54

class student:
    def __init__(self,name,rollno):
         self.name = name
         self.rollno = rollno
         self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu ='i5'
            self.ram = 6
        def show(self):
             print(self.brand,self.cpu,self.ram)

s1=student('Aravind',3)
s2=student('krishna',4)

s1.show()
#s2.show()

#lap1 = s1.lap
#lap2 = s2.lap
#lap=student.Laptop()
#print(id(lap1))
#rint(id(lap2))
