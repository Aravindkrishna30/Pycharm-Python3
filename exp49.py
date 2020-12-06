# 55/#51
class computer:
    #pass
    def __init__(self):
        self.name = "Aravind"
        self.age = 20

    def update(self):
        self.age =30

    def compare(self, others):
        if self.age == others.age:
            return True
        else:
            return False

c1= computer()
c2= computer()

c1.name = "krishna"
c1.age = 12


if c1.compare(c2):
    print("they are same")
else:
    print("They are Difference")


c1.update()
print("Name = ", c1.name)
print("Age =", c1.age)
print("Name = ", c2.name)
print("Age =", c2.age)

