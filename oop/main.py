# //classes in oop

# class Factory:
#     a = 12 #attribute

#     def hello(self): #method
#         print("Hello World")

#     print("hello how are i am getting intialized")   


# # print(Factory().a)    

# # Factory().hello()

# obj = Factory()
# print(obj.hello())

# class Factory:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"My name is {self.name} and my age is {self.age}")    

# alice = Factory("Alice", 30)
# mahamud = Factory("Mahmud", 25)

# print(alice.name)  # Output: Alice

# mahamud.show()  # Output: My name is Mahmud and my age is 25

# class Animal:
#     name = "lion" #class attribute

#     def __init__(self, age):   
#         self.age = age          # instance attribute

#     def show(self):
#         print("how are you")
    
#     @classmethod
#     def hello(cls):
#         print("Hello, I am an animal!")#class method

#     @staticmethod
#     def static():
#         print("I am a static method")#static method

# obj = Animal(5)
# obj.show()  # Output: how are you


# inheritance
class FactoryDhaka:  #parent class / super class
    a = "I am an attribute of Animal class" #class attribute
    def hello(self):
        print("Hello I am method from Animal class") #method

class FactoryChittagong(FactoryDhaka): #child class  / sub class
    pass

obj = FactoryDhaka()

obj2 = FactoryChittagong()

print(obj2.hello())  # Output: Hello I am method from Animal class

print(obj.a)  # Output: I am an attribute of Animal class