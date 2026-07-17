# Polymorphism

## ১. Polymorphism কী?

* **Polymorphism** শব্দের অর্থ **অনেক রূপ (Many Forms)**।
* Programming-এ **Polymorphism** বলতে বোঝায়, একই **Interface** বা **Method Name** বিভিন্ন Object বা Context অনুযায়ী ভিন্নভাবে কাজ করতে পারে।
* **Real-life Analogy:** আমরা সবাই ভোট দিতে পারি—কিন্তু কেউ আঙুলের ছাপ দিয়ে, কেউ EVM দিয়ে, আবার কেউ Postal Ballot-এর মাধ্যমে। কাজ একই, কিন্তু করার পদ্ধতি ভিন্ন।

---

# ২. Python-এ Polymorphism-এর ধরন

> **💡 মনে রাখো:** Compile-time Language (যেমন Java, C++)-এ বিভিন্ন ধরনের Polymorphism থাকে। Python-এ **Method Overloading** সরাসরি Support করে না। একই নামে একাধিক Method লিখলে শেষের Definition আগেরটিকে Overwrite করে দেয়।

| ধরন                | Python-এর Support | ব্যাখ্যা                                              |
| ------------------ | ----------------- | ----------------------------------------------------- |
| Method Overriding  | ✅ হ্যাঁ           | Child Class Parent Class-এর Method Override করে       |
| Duck Typing        | ✅ হ্যাঁ           | Object-এর Type নয়, Method আছে কিনা সেটি গুরুত্বপূর্ণ |
| Method Overloading | ❌ না              | শেষের Method Definition আগেরটিকে Overwrite করে        |

---

# ৩. Method Overriding — Runtime Polymorphism

Child Class যখন Parent Class-এর একই নামে নিজের Method তৈরি করে, তখন Runtime-এ Python সিদ্ধান্ত নেয় কোন Method Call হবে।

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

class Duck(Animal):
    def sound(self):
        print("Duck quacks")


# Polymorphism-এর মাধ্যমে একই Loop-এ সব Object ব্যবহার করা যায়
animals = [Animal(), Dog(), Cat(), Duck()]

for animal in animals:
    animal.sound()

# Output:
# Animal makes a sound
# Dog barks
# Cat meows
# Duck quacks
```

---

# ৪. Duck Typing — Python-এর মূল দর্শন

* **Philosophy:** *"If it walks like a duck and quacks like a duck, then it's a duck."*
* Python Object-এর **Type** দেখে না, বরং প্রয়োজনীয় **Method** আছে কিনা সেটি দেখে।

```python
class Duck:
    def talk(self):
        print("Quack!")

class Human:
    def talk(self):
        print("Hello!")

class Dog:
    def talk(self):
        print("Woof!")


def make_sound(obj):
    obj.talk()


make_sound(Duck())
# Quack!

make_sound(Human())
# Hello!

make_sound(Dog())
# Woof!
```

> **💡 Key Insight:** `make_sound()` Function-এর কাছে Object `Duck`, `Human`, নাকি `Dog`—তা গুরুত্বপূর্ণ নয়। গুরুত্বপূর্ণ হলো Object-এর মধ্যে `.talk()` Method আছে কিনা। এটিই **Duck Typing**।

---

# ৫. Method Overloading — Python-এ যেভাবে করা হয়

```python
# ❌ Python-এ Method Overloading কাজ করে না
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


calc = Calculator()

# calc.add(2, 3)
# ❌ TypeError — ৩টি Argument প্রয়োজন

print(calc.add(2, 3, 4))
# 9
```

উপরের উদাহরণে দ্বিতীয় `add()` Method প্রথমটিকে Overwrite করে দিয়েছে।

### ✅ Python-এ সঠিক উপায়

```python
class Calculator:
    def add(self, *args):
        return sum(args)


calc = Calculator()

print(calc.add(2, 3))
# 5

print(calc.add(2, 3, 4))
# 9

print(calc.add(1, 2, 3, 4))
# 10
```

> **💡 Tip:** Python-এ Method Overloading-এর পরিবর্তে সাধারণত `*args`, `**kwargs`, অথবা Default Parameter ব্যবহার করা হয়।

---

# ৬. Operator Overloading — Magic Methods দিয়ে

Python-এর Operator (`+`, `-`, `*` ইত্যাদি)-এর আচরণ নিজের Class-এর জন্য পরিবর্তন করা যায়। একে **Operator Overloading** বলা হয়।

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v3)

# Output:
# Vector(4, 6)
```

এখানে `v1 + v2` লিখলে Python স্বয়ংক্রিয়ভাবে `__add__()` Method Call করে।

---

# ৭. বাস্তব উদাহরণ — Shape Area Calculator

```python
class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Polymorphism: একই Loop-এ সব Shape ব্যবহার করা যায়
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area()}")

# Output:
# Circle: Area = 78.5
# Rectangle: Area = 24
# Triangle: Area = 12.0
```

এখানে প্রতিটি Object-এর জন্য একই `area()` Method Call করা হয়েছে, কিন্তু প্রতিটি Class নিজের মতো করে ফলাফল দিয়েছে। এটাই **Polymorphism**।

---

# ৮. Quick Reference

| Concept              | সংজ্ঞা                                          | Python-এ ব্যবহার                                          |
| -------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| Method Overriding    | Child Class Parent Class-এর Method Override করে | ✅ সবচেয়ে বেশি ব্যবহৃত                                    |
| Duck Typing          | Object-এর Type নয়, Method দেখে কাজ করে         | ✅ Python-এর Default Philosophy                            |
| Method Overloading   | একই নামে একাধিক Method                          | ❌ সরাসরি Support নেই (`*args` দিয়ে করা হয়)              |
| Operator Overloading | Operator-এর আচরণ পরিবর্তন করা                   | ✅ Magic Methods (`__add__`, `__sub__`, `__mul__` ইত্যাদি) |

---

# সারসংক্ষেপ

| Topic                | কী শেখা হলো                                                                             |
| -------------------- | --------------------------------------------------------------------------------------- |
| Polymorphism         | একই Interface বা Method বিভিন্ন Object-এর জন্য ভিন্নভাবে কাজ করতে পারে।                 |
| Method Overriding    | Child Class Parent-এর Method নিজের মতো করে লিখতে পারে।                                  |
| Duck Typing          | Python Type নয়, প্রয়োজনীয় Method আছে কিনা সেটি দেখে।                                 |
| Method Overloading   | Python সরাসরি Support করে না; `*args`, `**kwargs` বা Default Parameter ব্যবহার করা হয়। |
| Operator Overloading | Magic Method ব্যবহার করে Operator-এর আচরণ পরিবর্তন করা যায়।                            |

> **💡 মনে রাখবে:** Polymorphism-এর মূল উদ্দেশ্য হলো **একই Interface ব্যবহার করে বিভিন্ন Object-এর জন্য ভিন্ন আচরণ (Behavior) প্রদান করা**, ফলে Code আরও **Flexible**, **Reusable**, এবং **Maintainable** হয়।
