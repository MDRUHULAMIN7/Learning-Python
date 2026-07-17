
# Inheritance

## ১. Inheritance কী?

* সাধারণ অর্থে **Inheritance** মানে উত্তরাধিকার বা সম্পত্তি, যা পূর্বপুরুষ থেকে উত্তরসূরির কাছে যায়।
* Python-এ **Inheritance** হলো একটি **Class** থেকে অন্য একটি **Class**-এর **Attributes** ও **Methods** গ্রহণ করার প্রক্রিয়া।
* **Parent Class (Base Class):** যে Class থেকে Inherit করা হয়।
* **Child Class (Derived Class):** যে Class Inherit করে।

### সুবিধা

* **Code Reusability** — একই কোড বারবার লিখতে হয় না।
* **Organized Structure** — বড় প্রোগ্রাম সহজে গুছিয়ে রাখা যায়।
* **Easy to Maintain & Extend** — কোড সহজে পরিবর্তন ও নতুন Feature যোগ করা যায়।

---

# ২. Inheritance Syntax

```python
class Parent:
    def speak(self):
        print("I can speak!")

class Child(Parent):   # Parent Class থেকে Inherit করা হয়েছে
    pass

c = Child()
c.speak()
# Output: I can speak!
```

> **💡 Key Rule:** Child Class কোনো Parent Class Inherit করলে Parent Class-এর সব **Attribute** এবং **Method** স্বয়ংক্রিয়ভাবে ব্যবহার করতে পারে।

---

# ৩. Constructor in Inheritance

## ৩.১ Parent-এর Constructor Child-এর Object-এর সাথেও কাজ করে

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f"My name is {self.name}")

c = Child("Ruhul")
c.display()

# Output:
# My name is Ruhul
```

এখানে `Child`-এর নিজস্ব `__init__()` নেই, তাই Python স্বয়ংক্রিয়ভাবে `Parent`-এর `__init__()` ব্যবহার করেছে।

---

## ৩.২ Child-এর নিজস্ব Constructor থাকলে `super()` দিয়ে Parent-এর Constructor কল করতে হয়

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

c = Child("Ruhul", 21)
c.display()

# Output:
# My name is Ruhul, and I am 21 years old.
```

> **💡 `super()` বোঝো:** `super()` Parent Class-কে নির্দেশ করে। `super().__init__(name)` লিখলে Parent Class-এর `__init__()` Method Execute হয় এবং Parent-এর Attribute-গুলো Initialize হয়ে যায়।

---

# ৪. Method Overriding

যখন Child Class Parent Class-এর একই নামে নিজের একটি Method তৈরি করে, তখন Parent-এর Method-এর পরিবর্তে Child-এর Method চালু হয়। এটিকে **Method Overriding** বলা হয়।

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
# Animal makes a sound

d.sound()
# Dog barks

c.sound()
# Cat meows
```

---

# ৫. Types of Inheritance

## ৫.১ Single Inheritance

একটি Parent Class এবং একটি Child Class।

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

Child().greet()

# Output:
# Hello from Parent
```

---

## ৫.২ Multiple Inheritance

দুটি বা একাধিক Parent Class থেকে একটি Child Class Inherit করে।

```python
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def show(self):
        print("I have multiple skills")

c = Child()

c.show()
# I have multiple skills

c.skills()
# Coding
```

> **⚠️ MRO (Method Resolution Order):** Multiple Inheritance-এ একই নামে Method থাকলে Python প্রথমে যেই Parent Class Inherit করা হয়েছে, তার Method ব্যবহার করে। `Child.__mro__` দিয়ে Method Resolution Order দেখা যায়।

---

## ৫.৩ Multilevel Inheritance

ধাপে ধাপে Inheritance।

```python
class Grandparent:
    def heritage(self):
        print("Heritage from Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.heritage()

# Output:
# Heritage from Grandparent
```

---

## ৫.৪ Hierarchical Inheritance

একটি Parent Class থেকে একাধিক Child Class তৈরি হয়।

```python
class Animal:
    def breathe(self):
        print("শ্বাস নিচ্ছি")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

d = Dog()
c = Cat()

d.breathe()
# শ্বাস নিচ্ছি

d.bark()
# Woof!

c.breathe()
# শ্বাস নিচ্ছি

c.meow()
# Meow!
```

---

| Type         | Structure | উদাহরণ                       |
| ------------ | --------- | ---------------------------- |
| Single       | A → B     | Parent → Child               |
| Multiple     | A, B → C  | Father, Mother → Child       |
| Multilevel   | A → B → C | Grandparent → Parent → Child |
| Hierarchical | A → B, C  | Animal → Dog, Cat            |

---

# ৬. `isinstance()` ও `issubclass()`

```python
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
```

### ব্যাখ্যা

* `isinstance(object, Class)` → Object নির্দিষ্ট Class-এর Instance কি না তা পরীক্ষা করে।
* `issubclass(Child, Parent)` → একটি Class অন্য একটি Class-এর Child কি না তা পরীক্ষা করে।

---

# ৭. বাস্তব উদাহরণ — Employee System

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} | Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        super().show()
        print(f"Department: {self.department}")


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, stipend)

    def show(self):
        print(f"Intern: {self.name} | Stipend: {self.salary}")


m = Manager("Ruhul", 50000, "Engineering")
i = Intern("Foysal", 10000)

m.show()

# Ruhul | Salary: 50000
# Department: Engineering

i.show()

# Intern: Foysal | Stipend: 10000
```

---

# সারসংক্ষেপ

| Topic                    | কী শেখা হলো                                                    |
| ------------------------ | -------------------------------------------------------------- |
| Inheritance              | একটি Class অন্য Class-এর Attribute ও Method ব্যবহার করতে পারে। |
| Parent Class             | যে Class থেকে Inherit করা হয়।                                 |
| Child Class              | যে Class Inherit করে।                                          |
| `super()`                | Parent Class-এর Method বা Constructor কল করতে ব্যবহৃত হয়।     |
| Method Overriding        | Child Class Parent-এর একই Method নিজের মতো করে লিখতে পারে।     |
| Single Inheritance       | একটি Parent → একটি Child                                       |
| Multiple Inheritance     | একাধিক Parent → একটি Child                                     |
| Multilevel Inheritance   | Grandparent → Parent → Child                                   |
| Hierarchical Inheritance | একটি Parent → একাধিক Child                                     |
| `isinstance()`           | কোনো Object নির্দিষ্ট Class-এর Instance কি না পরীক্ষা করে।     |
| `issubclass()`           | একটি Class অন্য Class-এর Child কি না পরীক্ষা করে।              |

> **💡 মনে রাখবে:** Inheritance-এর মূল উদ্দেশ্য হলো **Code Reusability**, **Maintainability**, এবং **Extensibility** বৃদ্ধি করা। Parent Class-এর বিদ্যমান Code পুনরায় ব্যবহার করে Child Class সহজে নতুন Feature যোগ করতে পারে।
