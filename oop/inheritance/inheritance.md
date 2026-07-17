# Inheritance

## ১. Inheritance কী?

- সাধারণ অর্থে Inheritance মানে সম্পত্তি বা গুণ যা उত্তরসূরির কাছে যায়।
- Python ঎ Inheritance হলো এক Class থেকে আরেক Class ঎র Attributes ও Methods গ্রহণ করা।
- **Parent Class** (Base Class) যে class থেকে inherit করা হয়
- **Child Class** (Derived Class) যে class inherit করে
- **সুবিধা:**
    - Code Reusability — একই code বারবার লিখতে হয় না
    - Organized Structure — বড় প্রোগ্রাম সাজানো সহজ
    - Easy to Maintain ও Extend করা

## ২. Inheritance Syntax

```
class Parent:
    def speak(self):
        print('I can speak!')

class Child(Parent):   # তৃতীয় ব্রাকেট ঊ Parent class
    pass

c = Child()
c.speak()   # Output: I can speak! — Parent ঊর method Child পেয়েছে
```

> **💡 Key Rule:** Child class inherit করলে Parent class ঊর সব attribute ও method Child স্বয়ংক্রিয়ভাবে access করতে পারে।
> 

## ৩. Constructor in Inheritance

### ৩.১ Parent ঊর Constructor Child ঊর object ঊর সাথেও কাজ করে:

```
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f'My name is {self.name}')   # Parent ঊর attribute ব্যবহার

c = Child('Ruhul')
c.display()   # My name is Ruhul
```

### ৩.২ Child ঊর নিজস্ব Constructor থাকলে — `super()` দিয়ে Parent ডাকা

```
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # Parent ঊর __init__ ডাকা হলো
        self.age = age           # Child ঊর নিজস্ব attribute

    def display(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')

c = Child('Ruhul', 21)
c.display()   # My name is Ruhul, and I am 21 years old.
```

> **💡 `super()` বোঝো:** `super()` মানে Parent class কে টার্গেট করা। `super().__init__(name)` মনে Parent ঊর `__init__` জব রুন করো, Parent ঊর attribute সেট হয়ে যায়।
> 

## ৪. Method Overriding

Child class ঊ parent class ঊর method ঊর একই নামে নিজস্ব method তৈরি করলে Child ঊর version override হয়।

```
class Animal:
    def sound(self):
        print('Animal makes a sound')

class Dog(Animal):
    def sound(self):             # Override করা হলো
        print('Dog barks')

class Cat(Animal):
    def sound(self):             # Override করা হলো
        print('Cat meows')

a = Animal()
d = Dog()
c = Cat()

a.sound()   # Animal makes a sound
d.sound()   # Dog barks
c.sound()   # Cat meows
```

## ৫. Types of Inheritance

### ৫.১ Single Inheritance — একটি Parent, একটি Child

```
class Parent:
    def greet(self):
        print('Hello from Parent')

class Child(Parent):
    pass

Child().greet()   # Hello from Parent
```

### ৫.২ Multiple Inheritance — ২টি Parent, একটি Child

```
class Father:
    def skills(self):
        print('Coding')

class Mother:
    def skills(self):
        print('Cooking')

class Child(Father, Mother):   # দুটো Parent
    def show(self):
        print('I have multiple skills')

c = Child()
c.show()      # I have multiple skills
c.skills()    # Coding — Father ঊর method প্রাধান্য পাতিলো (MRO)
```

> **⚠️ MRO (Method Resolution Order):** Multiple Inheritance ঊ একই নামে method থাকলে Python **প্রথম Inherit করা Class ঊর method** ব্যবহার করে। `Child.__mro__` দিয়ে order দেখা যায়।
> 

### ৫.৩ Multilevel Inheritance — ধাপে ধাপে

```
class Grandparent:
    def heritage(self):
        print('Heritage from Grandparent')

class Parent(Grandparent):   # Grandparent থেকে inherit
    pass

class Child(Parent):         # Parent থেকে inherit
    pass

c = Child()
c.heritage()   # Heritage from Grandparent — ধাপে ধাপে পাওয়া গেল
```

### ৫.৪ Hierarchical Inheritance — এক Parent, বাদে বাদে Child

```
class Animal:
    def breathe(self):
        print('শ্বাস নিচ্ছি')

class Dog(Animal):
    def bark(self):
        print('Woof!')

class Cat(Animal):
    def meow(self):
        print('Meow!')

d = Dog()
c = Cat()

d.breathe()   # শ্বাস নিচ্ছি
d.bark()      # Woof!
c.breathe()   # শ্বাস নিচ্ছি
c.meow()      # Meow!
```

| Type | Structure | উদাহরণ |
| --- | --- | --- |
| Single | A → B | Parent → Child |
| Multiple | A, B → C | Father, Mother → Child |
| Multilevel | A → B → C | Grandparent → Parent → Child |
| Hierarchical | A → B, C | Animal → Dog, Cat |

## ৬. `isinstance()` ও `issubclass()`

```
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True — Dog, Animal ঊর instance!
print(issubclass(Dog, Animal)) # True
print(issubclass(Animal, Dog)) # False
```

## ৭. বাস্তব উদাহরণ — Employee System

lass Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def show(self):
        print(f'{self.name} | Salary: {self.salary}')

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        super().show()   # Parent show() ডাকা
        print(f'Department: {self.department}')

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, stipend)

    def show(self):
        print(f'Intern: {self.name} | Stipend: {self.salary}')

m = Manager('Ruhul', 50000, 'Engineering')
i = Intern('Foysal', 10000)

m.show()
# Ruhul | Salary: 50000
# Department: Engineering

i.show()
# Intern: Foysal | Stipend: 10000