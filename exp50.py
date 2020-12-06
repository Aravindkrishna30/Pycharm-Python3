#56/#56->Types of variable
class car:
    wheels = 4
    def __init__(self):
        self.mil =10
        self.compy = "BMW"

c1=car()
c2=car()
c1.mil = 15
#car.wheels = 5

print("Company :", c1.compy,"| miles=", c1.mil,"| wheels= ",c1.wheels)
print("Company :", c2.compy,"| miles=", c2.mil,"| wheels= ",c2.wheels)