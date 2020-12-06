# 54/#50
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        #print("in init")
    def config(self):
        #print("i5,16gb,1TB")
        print("config is :",self.cpu,self.ram)

com1 = computer('i5','16')
com2 = computer('Rysen 3','9')

com1.config()
com2.config()

