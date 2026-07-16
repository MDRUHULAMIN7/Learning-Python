# OOP in Python

## # Programming Approach — OOP কেন দরকার?

৩টি পদ্ধতিতে দুটি সংখ্যা যোগ করা যায় — প্রতিটির সুবিধা-অসুবিধা দেখো:

### * Imperative Approach (সরাসরি variable)

```
a = 12
b = 12
print(a + b)   # Output: 24
```

সমস্যা: আরো দুটি সংখ্যা যোগ করতে হলে আরো ২টি variable লিখতে হবে — বড় প্রোগ্রামে অব্যবহারি।

### * Functional Approach (ফাংশন)

```
def addition(a, b):
    return a + b

print(addition(12, 12))   # 24
print(addition(45, 45))   # 90
```

সুবিধা: বারবার call করা যায়। সমস্যা: বড় প্রোগ্রামে সব ফাংশন একসাথে manage করা কঠিন হয়, data ও logic আলাদা থাকে।

### * Object-Oriented Approach (OOP)

```
class Addition:
    def __init__(self, a, b):
        print(a + b)

obj = Addition(12, 12)   # Output: 24
```

সুবিধা: Data ও logic একত্রে, real-world অনুধাবনে, বড় প্রোগ্রাম manage করা সহজ।

| Approach | বিশেষত্ব | ব্যবহার |
| --- | --- | --- |
| Imperative | সরাসরি variable | বাড়ানো কঠিন |
| Functional | ফাংশনে ভাগ করা | Medium size প্রোগ্রাম |
| OOP | Object দিয়ে ভাবা | Real-world, বড় প্রোগ্রাম |

## # OOP কী?

- **OOPS (Object-Oriented Programming System)** হলো একটি programming paradigm যেখানে সব কিছু **Object** আকারে ভাবা হয়।
- প্রতিটি Object ঎ দুটো জিনিস থাকে:
    - **Data (Attributes)** — Object টি কী ধারণ করে
    - **Code (Methods)** — Object টি কী করতে পারে
- **OOP ঎র ৪ মূল নীতি (Pillars):**
    1. Encapsulation — data লুকিয়ে রাখা
    2. Inheritance — গুণাগুণ inherit করা
    3. Polymorphism — এক নাম, নানা রূপ
    4. Abstraction — দরকারি কিছু দেখানো, বাকি লুকানো

## 🗓️ অধ্যায়সমূহ

1. 🟦 **Classes** — Blueprint, Attributes, Methods, `self`
2. 🟧 **Objects & `__init__`** — Constructor, Instance creation
3. 🟨 **Encapsulation** — Public, Private, Protected
4. 🟩 **Inheritance** — Single, Multiple, `super()`
5. 🟥 **Polymorphism** — Method Overriding, Duck Typing
6. ⬜ **Abstraction** — Abstract Class, Interface
7. ⬛ **Magic / Dunder Methods** — `__str__`, `__len__`, `__add__`

