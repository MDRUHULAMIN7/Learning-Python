class Animal:
    name = "Tiger"  #class Attributes


    def __init__(self,age):
        self.age = age    #instance Attributes

    def show(self):  #instance Method
        print(f"how are you bro {self.age}")

    @classmethod
    def hello(cls):  #class method
        print(f"hey {cls.name} bro")

    @classmethod
    def hello2():  #class method
        print(f"hey bro")
 
    
    @staticmethod
    def static(): #static method
        print("wow buttterfly")


obj = Animal(111)

obj.show()

obj.hello()
obj.static()
# obj.hello2()