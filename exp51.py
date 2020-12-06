
class student:

    school = "Anna University"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
        #  def get_m1(self):
        #     return self.m1

        #  def set_m1(self,value):
        #     self.m1=value

    @classmethod
    def getschool(cls):
       return cls.school
      
    @staticmethod
    def info():
        print("This is student class... in abc module")


s1=student(21,23,44)
s2=student(33,55,66)

#print(s1.m1)
print(s1.avg())
print(student.getschool())
student.info()
