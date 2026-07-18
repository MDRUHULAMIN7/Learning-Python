
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# class Duck(Animal):
#     def sound(self):
#         print("Duck quacks")


# # Polymorphism-এর মাধ্যমে একই Loop-এ সব Object ব্যবহার করা যায়
# animals = [Animal(), Dog(), Cat(), Duck()]

# for animal in animals:
#     animal.sound()

# # Python-এ পলিমরফিজম হলো একই মেথড/ইন্টারফেস দিয়ে ভিন্ন ভিন্ন ক্লাসের অবজেক্টকে আলাদা আলাদাভাবে ব্যবহার করার ক্ষমতা। jemon akhane method akta sound sei akoid method bivinno class   nijeder kaj korse mane alada alada kaj |


class Vector:
    def __init__(self, x, y):
        self.x = x #1
        self.y = y #2

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) #akane self.x holo 1 ar other.x holo 3 and self.y holo 2 and other.y holo 4
    

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v4 = v1 + v2 

print(v4)