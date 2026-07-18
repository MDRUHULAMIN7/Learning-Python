# Dunder Methods

## ১. Dunder Methods কী?

* **Dunder** = **D**ouble **Under**score — অর্থাৎ Method-এর নামের আগে ও পরে `__` থাকে।
* এগুলো Python-এর বিশেষ **Built-in Methods**, যা একটি Class-এর আচরণ (Behavior) Customize করতে দেয়।
* এগুলোকে **Magic Methods** বলেও পরিচিত।
* সাধারণত এগুলো নিজে Call করতে হয় না। নির্দিষ্ট কোনো Operation (যেমন `print()`, `len()`, `+`, `==`) করলে Python স্বয়ংক্রিয়ভাবে সংশ্লিষ্ট Dunder Method Call করে।

### সুবিধা

* নিজের Class-কে Built-in Type-এর মতো ব্যবহার করা যায়।
* `+`, `-`, `*`, `len()`, `print()`, `==` ইত্যাদির আচরণ নিজের মতো করে নির্ধারণ করা যায়।

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ravi")

print(p.name)

# Output:
# Ravi
```

> **💡 এখানে `Person("Ravi")` লিখলেই Python স্বয়ংক্রিয়ভাবে `__init__()` Method Call করে।**

---

# ২. সবচেয়ে বেশি ব্যবহৃত Dunder Methods

| Dunder Method  | কখন Call হয়                     | উদাহরণ            |
| -------------- | -------------------------------- | ----------------- |
| `__init__`     | Object তৈরির সময়                | `Person("Ruhul")` |
| `__str__`      | `print(obj)` বা `str(obj)`       | `print(p)`        |
| `__repr__`     | `repr(obj)` বা Debugging-এর সময় | `repr(p)`         |
| `__len__`      | `len(obj)`                       | `len(p)`          |
| `__add__`      | `obj1 + obj2`                    | `p1 + p2`         |
| `__sub__`      | `obj1 - obj2`                    | `p1 - p2`         |
| `__mul__`      | `obj1 * obj2`                    | `p1 * p2`         |
| `__eq__`       | `obj1 == obj2`                   | `p1 == p2`        |
| `__lt__`       | `obj1 < obj2`                    | `p1 < p2`         |
| `__gt__`       | `obj1 > obj2`                    | `p1 > p2`         |
| `__getitem__`  | `obj[index]`                     | `p[0]`            |
| `__contains__` | `item in obj`                    | `"Ruhul" in p`    |
| `__call__`     | `obj()`                          | `p()`             |
| `__del__`      | `del obj`                        | `del p`           |

---

# ৩. `__str__()` ও `__repr__()`

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Student: {self.name} | GPA: {self.gpa}"

    def __repr__(self):
        return f"Student(name='{self.name}', gpa={self.gpa})"


s = Student("Ruhul", 3.85)

print(s)
# Student: Ruhul | GPA: 3.85

print(repr(s))
# Student(name='Ruhul', gpa=3.85)

print(str(s))
# Student: Ruhul | GPA: 3.85
```

> **💡 পার্থক্য**
>
> * `__str__()` → User-এর জন্য সুন্দর ও সহজে পড়ার মতো Output।
> * `__repr__()` → Developer ও Debugging-এর জন্য বিস্তারিত Representation।

---

# ৪. `__len__()` — `len()` Customize করা

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


pl = Playlist(["Song A", "Song B", "Song C"])

print(len(pl))

# Output:
# 3
```

> **💡 `len(pl)` লিখলে Python স্বয়ংক্রিয়ভাবে `__len__()` Method Call করে।**

---

# ৫. `__add__()`, `__sub__()`, `__mul__()` — Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
# Vector(4, 6)

print(v2 - v1)
# Vector(2, 2)

print(v1 * 3)
# Vector(3, 6)
```

---

# ৬. `__eq__()`, `__lt__()`, `__gt__()` — Comparison Operators

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __str__(self):
        return f"{self.name} ({self.gpa})"


s1 = Student("Ruhul", 3.85)
s2 = Student("Foysal", 3.70)
s3 = Student("Toha", 3.85)

print(s1 == s3)
# True

print(s1 > s2)
# True

print(s2 < s1)
# True


students = [s1, s2, s3]

ranked = sorted(students, reverse=True)

for student in ranked:
    print(student)

# Ruhul (3.85)
# Toha (3.85)
# Foysal (3.70)
```

---

# ৭. `__getitem__()` ও `__contains__()`

```python
class Bag:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)


bag = Bag(["pen", "book", "phone"])

print(bag[0])
# pen

print(bag[2])
# phone

print("book" in bag)
# True

print("laptop" in bag)
# False

print(len(bag))
# 3
```

---

# ৮. `__call__()` — Object-কে Function-এর মতো Call করা

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))
# 10

print(triple(5))
# 15

print(double(10))
# 20
```

> **💡 `double(5)` লিখলে Python স্বয়ংক্রিয়ভাবে `double.__call__(5)` Execute করে।**

---

# ৯. বাস্তব উদাহরণ — Custom List Class

```python
class SmartList:
    def __init__(self, items=None):
        self.items = items or []

    def __str__(self):
        return f"SmartList{self.items}"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        return SmartList(self.items + other.items)

    def __eq__(self, other):
        return self.items == other.items


sl1 = SmartList([1, 2, 3])
sl2 = SmartList([4, 5, 6])

print(sl1)
# SmartList[1, 2, 3]

print(len(sl1))
# 3

print(sl1[0])
# 1

print(2 in sl1)
# True

print(sl1 + sl2)
# SmartList[1, 2, 3, 4, 5, 6]

print(sl1 == SmartList([1, 2, 3]))
# True
```

---

# ১০. Quick Reference

```python
class MyClass:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __getitem__(self, index):
        pass

    def __contains__(self, item):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass
```

---

# সারসংক্ষেপ

| Dunder Method    | কাজ                                              |
| ---------------- | ------------------------------------------------ |
| `__init__()`     | Object তৈরি হওয়ার সময় Initialize করে।          |
| `__str__()`      | `print(obj)`-এর জন্য সুন্দর Output দেয়।         |
| `__repr__()`     | Debugging-এর জন্য বিস্তারিত Representation দেয়। |
| `__len__()`      | `len(obj)` Customize করে।                        |
| `__add__()`      | `+` Operator-এর আচরণ নির্ধারণ করে।               |
| `__sub__()`      | `-` Operator-এর আচরণ নির্ধারণ করে।               |
| `__mul__()`      | `*` Operator-এর আচরণ নির্ধারণ করে।               |
| `__eq__()`       | `==` Comparison Customize করে।                   |
| `__lt__()`       | `<` Comparison Customize করে।                    |
| `__gt__()`       | `>` Comparison Customize করে।                    |
| `__getitem__()`  | `obj[index]` ব্যবহার করতে দেয়।                  |
| `__contains__()` | `item in obj` ব্যবহার করতে দেয়।                 |
| `__call__()`     | Object-কে Function-এর মতো Call করতে দেয়।        |
| `__del__()`      | Object Delete হওয়ার সময় Call হয়।              |

---

