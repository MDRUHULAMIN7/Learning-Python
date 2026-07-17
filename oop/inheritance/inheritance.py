

# | Topic                    | কী শেখা হলো                                                    |
# | ------------------------ | -------------------------------------------------------------- |
# | Inheritance              | একটি Class অন্য Class-এর Attribute ও Method ব্যবহার করতে পারে। |
# | Parent Class             | যে Class থেকে Inherit করা হয়।                                 |
# | Child Class              | যে Class Inherit করে।                                          |
# | `super()`                | Parent Class-এর Method বা Constructor কল করতে ব্যবহৃত হয়।     |
# | Method Overriding        | Child Class Parent-এর একই Method নিজের মতো করে লিখতে পারে।     |
# | Single Inheritance       | একটি Parent → একটি Child                                       |
# | Multiple Inheritance     | একাধিক Parent → একটি Child                                     |
# | Multilevel Inheritance   | Grandparent → Parent → Child                                   |
# | Hierarchical Inheritance | একটি Parent → একাধিক Child                                     |
# | `isinstance()`           | কোনো Object নির্দিষ্ট Class-এর Instance কি না পরীক্ষা করে।     |
# | `issubclass()`           | একটি Class অন্য Class-এর Child কি না পরীক্ষা করে।              |

# > **💡 মনে রাখবে:** Inheritance-এর মূল উদ্দেশ্য হলো **Code Reusability**, **Maintainability**, এবং **Extensibility** বৃদ্ধি করা। Parent Class-এর বিদ্যমান Code পুনরায় ব্যবহার করে Child Class সহজে নতুন Feature যোগ করতে পারে।


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

# class Father:
#     def expertise(self):
#         print("Farming")

# class Mother:
#     def skills(self):
#         print('Cooking')

# class Child(Father,Mother):
#     def show(self):
#         print(' i have multiple skills')

# child1 = Child()

# print(child1.skills(),child1.expertise())
# print(Child.__mro__)


#multilevel inheritance 

# class GrandParent:
#     def __init__(self,land,home):
#         self.land = land
#         self.home = home

# class Parent(GrandParent):
#     def __init__(self, land, home,bike):
#         super().__init__(land, home)
#         self.bike = bike

# class Child(Parent):
#     def __init__(self, land, home, bike,car):
#         super().__init__(land, home, bike)
#         self.car = car

# child1 = Child("land","home","bike","car")

# child2 = GrandParent()

# print(child2.bike)

# class Animal:
#     def breathe(self):
#         print("শ্বাস নিচ্ছি")

# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# class Cat(Animal):
#     def meow(self):
#         print("Meow!")

# d = Dog()
# c = Cat()

# d.breathe()
# # শ্বাস নিচ্ছি

# d.bark()
# # Woof!

# c.breathe()
# # শ্বাস নিচ্ছি

# c.meow()
# # Meow!

# `isinstance()` ও `issubclass()`

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))
# True

print(isinstance(d, Animal))
# True

print(issubclass(Dog, Animal))
# True

print(issubclass(Animal, Dog))
# False