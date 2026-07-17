# Attributes & Methods

## ১. Types of Attribute — ২ ধরন

### ১.১ Class Attribute

- Class ঊর ভেতরে সরাসরি define করা variable — `__init__` ঊর বাইরে
- সব Object ঎কটি একই value share করে

### ১.২ Instance Attribute

- `__init__` ঊর ভেতরে `self.name` দিয়ে define করা variable
- প্রতিটি Object ঊর নিজস্ব স্বতন্ত্র value থাকে

```
class Car:
    wheels = 4           # Class Attribute — সব Car ঊর চাকা ঊর সংখ্যা একই

    def __init__(self, color):
        self.color = color   # Instance Attribute — প্রতিটি Car ঊর রং আলাদা

c1 = Car('Red')
c2 = Car('Blue')

print(c1.wheels)   # 4 — shared
print(c2.wheels)   # 4 — shared
print(c1.color)    # Red — c1 ঊর নিজস্ব
print(c2.color)    # Blue — c2 ঊর নিজস্ব

# Class Attribute change হলে সব বদলায়:
Car.wheels = 6
print(c1.wheels)   # 6
print(c2.wheels)   # 6
```

| বিষয় | Class Attribute | Instance Attribute |
| --- | --- | --- |
| Define হয় | Class body ঊর ভেতরে | `__init__` ঊ `self.x = ...` |
| Shared? | ✅ সব Object share করে | ❌ প্রতিটি Object ঊর আলাদা |
| Access | `ClassName.attr` অথবা `obj.attr` | শুধু `obj.attr` |
| ব্যবহার | Shared config, counter | Per-object data |

## ২. Types of Methods — ৩ ধরন

### ২.১ Instance Method

- Object (instance) ঊর সাথে কাজ করে
- প্রথম parameter বাধ্যতমূলকভাবে `self`
- Instance attribute আড়া করতে পারে

```
class MyClass:
    def instance_method(self):
        print('This is an instance method')

obj = MyClass()
obj.instance_method()   # Output: This is an instance method
```

### ২.২ Class Method

- Class ঊর সাথে কাজ করে, Instance ঊর সাথে নয়
- `@classmethod` decorator দিতে হয়
- প্রথম parameter হলো `cls` (class নিজে)

```
class MyClass:
    @classmethod
    def class_method(cls):
        print('This is a class method')

MyClass.class_method()   # Class থেকে directly call করা যায়
obj = MyClass()
obj.class_method()       # Object থেকেও হয়
```

### ২.৩ Static Method

- Class বা Instance — কোনোটা আড়ায় না
- `@staticmethod` decorator দিতে হয়
- Regular function ঊর মতো, শুধু Class ঊর ভেতরে রাখা হয় (organize করার জন্য)

```
class MyClass:
    @staticmethod
    def static_method():
        print('This is a static method')

MyClass.static_method()   # Class থেকে
obj = MyClass()
obj.static_method()       # Object থেকেও
```

## ৩. তিনের তুলনা একসাথে

```
class Student:
    school = 'RPI'   # Class Attribute

    def __init__(self, name, gpa):
        self.name = name
        self.gpa  = gpa

    # Instance Method — self দরকার, instance ঠিক করে
    def show_info(self):
        print(f'{self.name} | GPA: {self.gpa} | School: {self.school}')

    # Class Method — cls দরকার, class-level data access
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        print(f'School বদলল: {cls.school}')

    # Static Method — কিছুই দরকার নেই, utility
    @staticmethod
    def is_passing(gpa):
        return gpa >= 2.5

s1 = Student('Ruhul', 3.85)
s2 = Student('Toha', 2.10)

s1.show_info()                    # Ruhul | GPA: 3.85 | School: RPI
Student.change_school('BUBT')     # School বদলল: BUBT
s1.show_info()                    # Ruhul | GPA: 3.85 | School: BUBT

print(Student.is_passing(3.85))   # True
print(Student.is_passing(2.10))   # False
```

| Method | Decorator | প্রথম Parameter | কোথায় Access করে |
| --- | --- | --- | --- |
| Instance Method | নেই | `self` | Instance + Class |
| Class Method | `@classmethod` | `cls` | শুধু Class |
| Static Method | `@staticmethod` | কিছু নেই | কিছুই না |

## ৪. Property Decorator — Attribute ঊর মতো Method Access

```
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):          # Method কিন্তু attribute ঊর মতো call হবে
        return 3.14 * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.area)       # 78.5 — () দরকার নেই!
print(c.diameter)   # 10
```

> **💡 `@property` কোথায় কাজ করে?** যখন কোনো value অন্য Attribute থেকে calculate হয় — attribute হিসেবে access করতে পারা সুবিধাজনক।
> 

## ৫. বাস্তব উদাহরণ — Temperature Converter

```
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius    # _ মানে convention অনুযায়ী private

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('অসম্ভব temperature!')
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @staticmethod
    def freeze_point():
        return 0   # Celsius ঊ পানি জমার বিন্দু

t = Temperature(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0
t.celsius = 0
print(t.fahrenheit)   # 32.0
print(Temperature.freeze_point())   # 0
```

## ৬. সর্বমোট Quick Reference

class Demo:
    class_attr = 'shared'          # Class Attribute

    def __init__(self, val):
        self.inst_attr = val       # Instance Attribute

    def inst_method(self):         # Instance Method
        return self.inst_attr

    @classmethod
    def cls_method(cls):           # Class Method
        return cls.class_attr

    @staticmethod
    def stat_method():             # Static Method
        return 'no context needed'

    @property
    def computed(self):            # Property
        return self.inst_attr.upper()