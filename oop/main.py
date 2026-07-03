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

class Factory:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and my age is {self.age}")    

alice = Factory("Alice", 30)
mahamud = Factory("Mahmud", 25)

print(alice.name)  # Output: Alice

mahamud.show()  # Output: My name is Mahmud and my age is 25