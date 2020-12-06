
from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class whirteboard:
    def write(self):
        print("Its writing")

class programmer:
    def work(self,com):
        print("solving problems")
        com.process()

#com=computer()
com1= laptop()
#com1.process()
#com.process()
prog=programmer()
prog.work(com1)