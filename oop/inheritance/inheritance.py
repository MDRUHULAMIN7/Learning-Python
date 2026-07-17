# class  Factory:
#     a = 'hello i am a attribute mentioned inside Factory'
#     def hello(self):
#         print ('hello i am a method mentioned inside Factory')

# class Factory2(Factory):
#     b = 22

# obj = Factory2()

# print(obj.a)

# class Men:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Men):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"hello your name is {self.name} and age is {self.age}")

# person1 = Human('Ruhul',33)
# person3 = Men('Amin')

# print(person1.show(),person1.age)
# print(person3.show())

#multiple inheritance 

class Father:
    def expertise(self):
        print("Farming")

class Mother:
    def skills(self):
        print('Cooking')

class Child(Father,Mother):
    def show(self):
        print(' i have multiple skills')

child1 = Child()

print(child1.skills(),child1.expertise())
print(Child.__mro__)
