#59/#55
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")
#class B:  #Multiple Inheritance
class B(A): #Single Level Inheritance
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")
#class C(A,B): #Multiple Inheritance
class C(B): #Multi Level Inheritance
    def feature5(self):
        print("Feature 5 working")

a=A()
a.feature1()
a.feature2()

b=B()
b.feature1()

c=C()
c.feature2()
