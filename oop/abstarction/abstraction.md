### Abstraction

### ১. Abstraction কী?

* Abstraction মানে জটিল বিষয় বা Implementation লুকিয়ে রেখে শুধু দরকারি অংশ বা Interface দেখানো।

* Real-life Analogy: গাড়ি চালাতে হলে Driver-এর ইঞ্জিনের ভেতরের জটিল কাজ জানা দরকার হয় না। সে শুধু Steering, Accelerator, Brake ইত্যাদি ব্যবহার করে।

* সুবিধা:

  * Complex System সহজে ব্যবহার করা যায়।

  * সব Subclass-এর জন্য একটি নির্দিষ্ট Interface তৈরি করা যায়।

  * Encapsulation ও Abstraction একসাথে বড় Program-কে আরও Organized করে।

* Python-এ Abstraction: Python-এ সরাসরি Built-in Abstract Class নেই। এটি `abc` Module-এর মাধ্যমে করা হয়।

### ২. Abstract Class ও Abstract Method

* Abstract Class: এমন একটি Class, যার মধ্যে এক বা একাধিক Abstract Method থাকে।

* Abstract Method: এমন Method, যা Define করা হয় কিন্তু Implement করা হয় না। Subclass-কে এটি Implement করতে বাধ্য করা হয়।

* Abstract Class থেকে Object তৈরি করা যায় না।

Python

Run

```
from abc import ABC, abstractmethod

class Animal(ABC):           # Abstract Class

    @abstractmethod
    def make_sound(self):    # Abstract Method
        pass


class Dog(Animal):

    def make_sound(self):
        print("Dog says Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Cat says Meow!")


d = Dog()
d.make_sound()

# Output:
# Dog says Woof!

c = Cat()
c.make_sound()

# Output:
# Cat says Meow!

# a = Animal()
# ❌ TypeError: Can't instantiate abstract class Animal
```

⚠️ মূল নিয়ম: কোনো Subclass যদি Abstract Method Implement না করে, তাহলে সেই Subclass থেকেও Object তৈরি করা যাবে না এবং `TypeError` আসবে।

### ৩. Abstract Class-এ Regular Method-ও থাকতে পারে

Abstract Class-এর মধ্যে শুধু Abstract Method নয়, সাধারণ Method-ও থাকতে পারে। Subclass চাইলে এগুলো Override করতে পারে, আবার সরাসরি Inherit করেও ব্যবহার করতে পারে।

Python

Run

```
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"রং: {self.color} | ক্ষেত্রফল: {self.area()}")


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)


class Rectangle(Shape):

    def __init__(self, color, w, h):
        super().__init__(color)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


c = Circle("Red", 5)
r = Rectangle("Blue", 4, 6)

c.describe()
# রং: Red | ক্ষেত্রফল: 78.5

r.describe()
# রং: Blue | ক্ষেত্রফল: 24

print(c.perimeter())
# 31.4

print(r.perimeter())
# 20
```

### ৪. Abstraction vs Encapsulation — পার্থক্য

| বিষয়    | Encapsulation         | Abstraction                      |
| -------- | --------------------- | -------------------------------- |
| মানে     | Data লুকিয়ে রাখা     | Complexity লুকিয়ে রাখা          |
| উদ্দেশ্য | Data সুরক্ষা          | Simple Interface দেওয়া          |
| ব্যবহার  | _, __ Access Modifier | Abstract Class ও Abstract Method |
| উদাহরণ   | ATM PIN লুকানো        | ATM Button দিয়ে টাকা তোলা       |

### ৫. বাস্তব উদাহরণ — Payment System

Python

Run

```
from abc import ABC, abstractmethod

class Payment(ABC):       # Abstract Payment Blueprint

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def receipt(self, amount):
        print(f"Receipt: {amount} টাকা Payment সম্পন্ন")


class BkashPayment(Payment):

    def pay(self, amount):
        print(f"bKash-এ {amount} টাকা Payment")
        self.receipt(amount)

    def refund(self, amount):
        print(f"bKash-এ {amount} টাকা Refund")


class NagadPayment(Payment):

    def pay(self, amount):
        print(f"Nagad-এ {amount} টাকা Payment")
        self.receipt(amount)

    def refund(self, amount):
        print(f"Nagad-এ {amount} টাকা Refund")


payments = [BkashPayment(), NagadPayment()]

for p in payments:
    p.pay(500)

# Output:
# bKash-এ 500 টাকা Payment
# Receipt: 500 টাকা Payment সম্পন্ন
# Nagad-এ 500 টাকা Payment
# Receipt: 500 টাকা Payment সম্পন্ন
```

এখানে `Payment` হলো Abstract Class। `BkashPayment` এবং `NagadPayment` একই Interface (`pay()` ও `refund()`) অনুসরণ করে, কিন্তু নিজ নিজ Implementation ব্যবহার করে।

### ৬. Quick Reference

Python

Run

```
from abc import ABC, abstractmethod

class MyAbstract(ABC):

    @abstractmethod
    def must_implement(self):
        pass

    def optional(self):
        print("Default behavior")
```

* `ABC` Inherit করতে হবে।

* `@abstractmethod` দিয়ে Abstract Method তৈরি করতে হবে।

* সব Subclass-কে `must_implement()` Method Implement করতে হবে।

* `optional()` হলো Regular Method, যা Subclass চাইলে Override করতে পারে।

### সারসংক্ষেপ

| Topic           | কী শেখা হলো                                                   |
| --------------- | ------------------------------------------------------------- |
| Abstraction     | জটিল Implementation লুকিয়ে রেখে দরকারি Interface দেখানো।     |
| Abstract Class  | এমন Class, যেখান থেকে সরাসরি Object তৈরি করা যায় না।         |
| Abstract Method | এমন Method, যা Subclass-কে অবশ্যই Implement করতে হয়।         |
| abc Module      | Python-এ Abstraction তৈরি করার জন্য ব্যবহৃত Module।           |
| ABC             | Abstract Base Class তৈরি করতে ব্যবহৃত হয়।                    |
| @abstractmethod | কোনো Method-কে Abstract Method হিসেবে ঘোষণা করতে ব্যবহৃত হয়। |

