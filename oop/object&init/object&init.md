Objects & **init**

## ১. Object কী?

- **Object** হলো Class এর blueprint থেকে তৈরি actual instance — যা দিয়ে বাস্তবে কাজ করা যায়।
- **Real-life Analogy — Bag Factory:**
    - **Bag Factory = Class** — blueprint বলে দিচ্ছে ব্যাগে কী কী লাগবে (material, zips, pockets)
    - **Reebok, Campus, Nike = Objects** — সেই blueprint দিয়ে নিজেদের মতো ব্যাগ তৈরি করেছে
    - প্রতিটি কোম্পানি ঊর ব্যাগে material, zips, pockets আলাদা — তেমনি প্রতিটি object নিজস্ব data রাখে

```
# Class = Blueprint (Bag Factory)
class Fruit:
    name = 'Apple'

# Object তৈরি — class কে variable ঊ দাও
f = Fruit()

# Object দিয়ে attribute access
print(f.name)   # Output: Apple
```

## ২. Object তৈরির Syntax

```
# Syntax
object_name = ClassName()

# উদাহরণ
class Car:
    brand = 'Toyota'
    color = 'Red'

    def drive(self):
        print(f'{self.brand} চলতেশে!')

# Object তৈরি
car1 = Car()   # car1 একটি Object / Instance
car2 = Car()   # car2 আরেকটি আলাদা Object

# দুটো object আলাদা, কিন্তু একই blueprint থেকে তৈরি
print(car1 is car2)   # False — আলাদা memory ঊ

car1.drive()   # Toyota চলতেশে!
```

> **💡 মনে রাখো:** একটি Class থেকে যত ইচ্ছে তত Object তৈরি করা যায় — প্রতিটি Object memory ঊ আলাদা জায়গা নেয়।
> 

## ৩. `__init__` — Constructor Method

- **`__init__`** হলো একটি বিশেষ method যা Object তৈরির সাথে সাথে স্বয়ংক্রিয়ভাবে call হয়।
- এটি Object কে **initialize** করে — অর্থাৎ প্রতিটি Object তৈরি হওয়ার সময় নিজের ডেটা সেট করে নেয়।
- `__init__` কে **Constructor** বলা হয়।

```
class Student:
    def __init__(self, name, age, gpa):   # Object তৈরির সাথে সাথে call হয়
        self.name = name    # Instance Attribute সেট হচ্ছে
        self.age = age
        self.gpa = gpa

# Object তৈরি — __init__ স্বয়ংক্রিয়ভাবে ডাকা হবে
s1 = Student('Ruhul', 21, 3.85)
s2 = Student('Foysal', 20, 3.70)

print(s1.name)   # Ruhul
print(s2.name)   # Foysal
print(s1.gpa)    # 3.85
```

## ৪. `__init__` Default Values

```
class Student:
    def __init__(self, name, age, gpa=0.0):   # gpa ঊর default = 0.0
        self.name = name
        self.age = age
        self.gpa = gpa

s1 = Student('Ruhul', 21, 3.85)   # gpa দেওয়া হয়েছে
s2 = Student('Toha', 22)          # gpa default 0.0 নেবে

print(s1.gpa)   # 3.85
print(s2.gpa)   # 0.0
```

## ৫. Object ঎র Attributes ও Methods Access

```
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f'{self.name} বলে: {self.sound}')

    def info(self):
        return f'Animal: {self.name}'

cat = Animal('Cat', 'Meow')
dog = Animal('Dog', 'Woof')

# Attribute access
print(cat.name)    # Cat
print(dog.sound)   # Woof

# Method call
cat.speak()   # Cat বলে: Meow
dog.speak()   # Dog বলে: Woof

# Method return value
result = cat.info()
print(result)     # Animal: Cat
```

## ৬. Object Attribute পরিবর্তন ও মুছে দেওয়া

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Ruhul', 21)
print(p.name)   # Ruhul

# Attribute Update
p.name = 'Ruhul Amin'
p.age = 22
print(p.name)   # Ruhul Amin

# নতুন Attribute যোগ করা (Runtime ঊ)
p.city = 'Rajshahi'
print(p.city)   # Rajshahi

# Attribute মুছে দেওয়া
del p.city
# print(p.city)   # ❌ AttributeError!

# hasattr() — Attribute আছে কিনা চেক
 print(hasattr(p, 'name'))   # True
print(hasattr(p, 'city'))   # False
```

## ৭. Built-in Functions যা Object ঎র সাথে কাজ করে

```
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

c = Car('Toyota', 120)

# type() — Object ঎র type জানা
print(type(c))             # <class '__main__.Car'>

# isinstance() — নির্দিষ্ট class ঊর instance কিনা
print(isinstance(c, Car))  # True

# dir() — Object ঊর সব attributes ও methods দেখা
 print(dir(c))

# vars() — Object ঊর instance attributes dict আকারে
print(vars(c))   # {'brand': 'Toyota', 'speed': 120}

# id() — Object ঊর memory address
print(id(c))   # কোনো সংখ্যা (memory location)
```

## ৮. Multiple Objects — নিজস্ব State

```
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get(self):
        return self.count

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c1.increment()

c2.increment()

print(c1.get())   # 3 — c1 ঊর নিজস্ব state
print(c2.get())   # 1 — c2 ঊর নিজস্ব state, c1 ঊর সাথে কোনো সম্পর্ক নেই
```

## ৯. `__str__` — Object কে সুন্দরভাবে Print করা

```
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):   # print() call হলে এটি ব্যবহার হবে
        return f'Student: {self.name} | GPA: {self.gpa}'

s = Student('Ruhul', 3.85)
print(s)   # Student: Ruhul | GPA: 3.85  (বাজে মেমোরি address না!)
```

## ১০. বাস্তব উদাহরণ — Student Management

```
class Student:
    total_students = 0   # Class Attribute — সবার shared

    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept
        Student.total_students += 1   # প্রতিটি object তৈরির সময় count বাড়ে

    def __str__(self):
        return f'[{self.roll}] {self.name} — {self.dept}'

    def update_dept(self, new_dept):
        self.dept = new_dept
        print(f'{self.name} ঊর dept update: {new_dept}')

    @classmethod
    def get_total(cls):
        return f'মোট Student: {cls.total_students}'

s1 = Student('Ruhul', '2301', 'Computer')
s2 = Student('Foysal', '2302', 'EEE')
s3 = Student('Toha', '2303', 'Civil')

print(s1)   # [2301] Ruhul — Computer
print(s2)   # [2302] Foysal — EEE

s1.update_dept('CSE')   # Ruhul ঊর dept update: CSE

print(Student.get_total())   # মোট Student: 3
```

## ১১. Class vs Object — Quick Comparison

| বিষয় | Class | Object |
| --- | --- | --- |
| সংজ্ঞা | Blueprint / Template | Blueprint থেকে তৈরি instance |
| Keyword | `class` | `ClassName()` |
| Memory | Define হলে ঊর memory নেয় | Object তৈরি হলে memory নেয় |
| সংখ্যা | একটি | যত ইচ্ছে তত |
| উদাহরণ | Bag Factory | Reebok, Nike, Adidas ঊর ব্যাগ |

## 🚀 পরবর্তী Topic

**Encapsulation** — Object ঊর data সুরক্ষিত রাখা — Public, Private, Protected concept পরের page ঎ আছে।