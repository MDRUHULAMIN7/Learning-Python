## 1. Class কী?

- **Class** হলো Object তৈরির একটি blueprint বা template।
- **Real-life Analogy:** Class হলো বাড়ির design plan (blueprint) — এতে থাকে বাড়িতে কতটি ঘর থাকবে, কতটি জানালা থাকবে সব বলা আছে। কিন্তু plan দিয়ে কিছু বাস করা যায় না — Object হলো actual বাড়ি যেটা সেই blueprint দিয়ে তৈরি।

## 2. Class Syntax

```
class ClassName:   # 'class' keyword + PascalCase নাম (OOP convention)
    attribute = value   # Class attribute

    def method(self):   # Method
        pass
```

```
# সরল উদাহরণ
class Car:
    brand = 'Toyota'   # Class attribute

print(Car.brand)   # Toyota — সরাসরি class থেকে আচ্ছেস
```

> **💡 Naming Convention:** Class ঎র নাম **PascalCase** ঊ লিখতে হয় — যেমন `Car`, `BankAccount`, `StudentRecord`। Function ঎র মতো `snake_case` নয়।
> 

## 3. Attributes ও Methods — Class ঊর দুটি Part

- **Attributes:** Class ঊর ভেতরে define করা variables — অর্থাৎ object জী কী data ধারণ করে
- **Methods:** Class ঊর ভেতরে define করা functions — অর্থাৎ object জী কী করতে পারে

```
class Animal:
    species = 'Cat'      # Attribute — data

    def sound(self):     # Method — function
        print('Meow!')
```

## 4. self — OOP ঊর সবচেয়ে গুরুত্বপূর্ণ keyword

- **`self`** হলো class থেকে তৈরি current object ঊর রেফারেন্স। প্রতিটি method ঊর প্রথম parameter হিসেবে `self` দিতে হয়।
- Python স্বয়ংক্রিয়ভাবে `self` ঊর জায়গায় current object pass করে।

```
class Dog:
    def bark(self):         # self = current object
        print('Woof!')

    def info(self, name):   # self + আরো parameter
        print(f'আমার নাম {name}')

dog1 = Dog()
dog1.bark()           # Python আসলে Dog.bark(dog1) ডাকে
dog1.info('Tommy')    # Dog.info(dog1, 'Tommy')
```

> **⚠️ গুরুত্বপূর্ণ:** `self` শুধু নাম, অন্য নামও দেওয়া যায় — কিন্তু **Python convention হলো `self`** ব্যবহার করা।
> 

## 5. Object তৈরি করা — Class থেকে Instance

Class হলো blueprint, **Object** হলো সেই blueprint থেকে তৈরি actual item।

```
class Animal:
    species = 'Cat'       # Class Attribute

    def sound(self):      # Method
        print('Meow!')

# Object / Instance তৈরি
a = Animal()

# Attribute access
print(Animal.species)    # Class থেকে সরাসরি: Cat
print(a.species)         # Object থেকে: Cat

# Method call
a.sound()   # Output: Meow!
```

## 6. Class Attribute vs Instance Attribute

```
class Student:
    school = 'RPI'   # Class Attribute — সব object share করে

    def __init__(self, name, age):   # Instance Attribute — প্রতিটি object ঊর নিজস্ব
        self.name = name
        self.age = age

s1 = Student('Ruhul', 21)
s2 = Student('Foysal', 20)

print(s1.name)    # Ruhul — s1 ঊর নিজস্ব
print(s2.name)    # Foysal — s2 ঊর নিজস্ব
print(s1.school)  # RPI — সবার shared
print(s2.school)  # RPI — একই

# Class attribute change হলে সবার পরিবর্তন হয়:
Student.school = 'BUBT'
print(s1.school)  # BUBT
print(s2.school)  # BUBT
```

| বিষয় | Class Attribute | Instance Attribute |
| --- | --- | --- |
| Define কোথায় | Class body তে | `__init__` method ঊ |
| সব object share? | ✅ হ্যাঁ | ❌ না, প্রতিটি object ঊর আলাদা |
| Access | `ClassName.attr` / `obj.attr` | `obj.attr` / `self.attr` |

## 7. Class ঊর Method ঊর প্রকারভেদ — ৩ ধরন

```
class MyClass:
    class_var = 0

    # 1. Instance Method — সবচেয়ে সাধারণ, self দরকার
    def instance_method(self):
        return f'Instance method: {self.class_var}'

    # 2. Class Method — class ঊর data access করে, @classmethod দরকার
    @classmethod
    def class_method(cls):
        cls.class_var += 1
        return f'Class method: {cls.class_var}'

    # 3. Static Method — class/instance কিছুই access করে না, utility ফাংশন
    @staticmethod
    def static_method():
        return 'Static method: কোনো context দরকার নেই'

obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
```

## 8. বাস্তব উদাহরণ — BankAccount Class

```
class BankAccount:
    bank_name = 'Sonali Bank'   # Class Attribute

    def __init__(self, owner, balance=0):
        self.owner = owner       # Instance Attribute
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} টাকা জমা হয়েছে। বাকি: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('ব্যালেন্স কম!')
        else:
            self.balance -= amount
            print(f'{amount} টাকা তোলা হয়েছে। বাকি: {self.balance}')

    def get_info(self):
        print(f'{self.bank_name} | মালিক: {self.owner} | ব্যালেন্স: {self.balance}')

# Object তৈরি
acc1 = BankAccount('Ruhul', 5000)
acc2 = BankAccount('Foysal')

acc1.deposit(2000)    # 2000 টাকা জমা হয়েছে। বাকি: 7000
acc1.withdraw(1000)   # 1000 টাকা তোলা হয়েছে। বাকি: 6000
acc1.get_info()       # Sonali Bank | মালিক: Ruhul | ব্যালেন্স: 6000
acc2.get_info()       # Sonali Bank | মালিক: Foysal | ব্যালেন্স: 0
```

## 9. বোঝার জন্য Quick Summary

```
# এক নজরে Class ঊর সব জিনিস

class Person:                     # Class definition
    species = 'Human'             # Class Attribute

    def __init__(self, name):     # Constructor / Instance Attribute
        self.name = name

    def greet(self):              # Instance Method
        print(f'হ্যালো, আমি {self.name}')

    @classmethod
    def info(cls):                # Class Method
        print(f'Species: {cls.species}')

    @staticmethod
    def utility():                # Static Method
        print('Utility function')

# Object তৈরি ও ব্যবহার
p = Person('Ruhul')
p.greet()            # হ্যালো, আমি Ruhul
Person.info()        # Species: Human
Person.utility()     # Utility function
print(p.name)        # Ruhul
print(Person.species) # Human
```

## 10. Best Practices

- **PascalCase** দিয়ে Class ঊর নাম দাও — `BankAccount`, `StudentRecord`
- **Docstring** দাও — class কী করে বর্ণনা করো
- **Single Responsibility** — প্রতিটি class ঊর ঊর ঎কটা নির্দিষ্ট কাজ থাকুক
- **`self.attr` vs `ClassName.attr`** পার্থক্য বোঝো

## 🚀 পরবর্তী Topic

**Objects ও `__init__` Constructor** — Class থেকে Object কীভাবে তৈরি হয়, `__init__` কীভাবে কাজ করে সেটা পরের page এ আছে।