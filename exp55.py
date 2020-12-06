
class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("Ru nning")

class Laptop:
    def code(self,ide):
        ide.execute()

#ide=pycharm()
ide=MyEditor()

lap=Laptop()
lap.code(ide)