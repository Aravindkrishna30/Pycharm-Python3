#Method Overriding
class A:
    def show(self):
        print("in A Show")

class B(A):
    def show(self):
        print("in B Show")


a= B()
a.show()