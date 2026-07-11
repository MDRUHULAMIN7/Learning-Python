Python Tuple

## ১. Tuple কী এবং কেন ব্যবহার করি?

- **Definition:** Tuple হলো Python এর একটি Ordered, Immutable data structure যা `( )` parenthesis দিয়ে তৈরি হয়। List ঎র মতোই, তবে একবার তৈরি হলে পরিবর্তন করা যায় না।
- **Real-life Analogy:** তোমার জন্মতারিখ এবং নাম বারবার পরিবর্তন হয় না — এটাই Tuple ঎র মতো। যা নির্দিষ্ট এবং পরিবর্তন হওয়া উচিত নয়, তা Tuple ঎ রাখো।
- **কোথায় Tuple ব্যবহার হয়?**
    - Database record — একটি row ঎র data (id, name, age) পরিবর্তন হওয়া উচিত নয়
    - Geographic coordinates — latitude, longitude
    - Function থেকে multiple values return করা
    - Dictionary ঎র key হিসেবে (List key হয় না, Tuple হয়)
    - Constant data যা protect করতে চাও

## ২. Tuple ঎র ৪টি মূল বৈশিষ্ট্য (Powers)

### ২.১ Immutable — পরিবর্তন করা যায় না

Tuple তৈরির পরে কোনো element যোগ, বিয়োগ বা বদলানো যায় না। তোমার data সুরক্ষিত থাকে।

```
t = (10, 20, 30)
t[1] = 99   # ❌ TypeError: 'tuple' object does not support item assignment
```

### ২.২ Duplicates — একই মান বারবার থাকতে পারে

```
marks = (85, 90, 85, 72, 90)   # duplicate আছে, কোনো সমস্যা নেই
print(marks)   # (85, 90, 85, 72, 90)
```

### ২.৩ Ordered — ক্রম বজায় থাকে

Index দিয়ে নির্দিষ্ট element আচ্চেস করা যায়।

### ২.৪ Heterogeneous — মিশ্র data type

```
student = ('Ruhul', 21, 3.85, True, ['CS', 'Math'])   # সব ধরনের data এক Tuple ঎!
print(student)
```

## ৩. Tuple তৈরি করা (Creation)

```
# খালি Tuple
empty = ()
empty2 = tuple()

# সরাসরি তৈরি
fruits = ('apple', 'banana', 'cherry')
numbers = (1, 2, 3, 4, 5)

# ১টি মাত্র element — trailing comma দরকার!
single = (42,)         # ✅ সঠিক Tuple
not_tuple = (42)       # ❌ এটি শুধু int, Tuple নয়!
print(type(single))    # <class 'tuple'>
print(type(not_tuple)) # <class 'int'>

# Parenthesis ছাড়াও Tuple হয় (Tuple Packing)
packed = 1, 2, 3
print(type(packed))    # <class 'tuple'>

# List থেকে Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# range() থেকে Tuple
t = tuple(range(1, 6))   # (1, 2, 3, 4, 5)
```

> **⚠️ সবচেয়ে সাধারণ ভুল:** `single = (42)` লিখলে int হয়, Tuple হয় না। একটি element হলে `(42,)` বলতে হবে।
> 

## ৪. Indexing ও Slicing

List ঎র মতোই হুবহু একই নিয়ম।

```
fruits = ('apple', 'banana', 'cherry', 'mango', 'grape')
#           0         1         2         3        4
#          -5        -4        -3        -2       -1

# Positive Index
print(fruits[0])    # apple
print(fruits[-1])   # grape

# Slicing: tuple[start:stop:step]
print(fruits[1:4])    # ('banana', 'cherry', 'mango')
print(fruits[::-1])   # রিভার্স: ('grape', 'mango', 'cherry', 'banana', 'apple')
print(fruits[::2])    # ('apple', 'cherry', 'grape')
```

> **🧠 Expert Note:** Slicing একটি নতুন Tuple return করে — original অপরিবর্তিত থাকে।
> 

## ৫. Tuple Traversing (Loop দিয়ে)

```
fruits = ('apple', 'banana', 'cherry')

# Method 1: সরাসরি element
for fruit in fruits:
    print(fruit)

# Method 2: enumerate() — Expert Style
for index, fruit in enumerate(fruits):
    print(f'{index} -> {fruit}')
# Output:
# 0 -> apple
# 1 -> banana
# 2 -> cherry

# Method 3: while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

## ৬. Tuple ঎র Methods — মাত্র ২টি!

Tuple immutable হওয়ায় List ঎র মতো বহু method নেই। মাত্র ২টি method আছে:

```
t = (5, 2, 9, 1, 5, 6, 5)

# index() — প্রথম occurrence ঎র index বলে
print(t.index(9))    # 2
print(t.index(5))    # 0 — প্রথম 5 ঎র index

# count() — কতবার আছে গণনা করে
print(t.count(5))    # 3 — 5 তিনবার আছে
print(t.count(9))    # 1
```

| Method | কাজ | উদাহরণ |
| --- | --- | --- |
| `index(x)` | প্রথম occurrence ঎র index | `t.index(9)` → `2` |
| `count(x)` | কতবার আছে গণনা | `t.count(5)` → `3` |

### Built-in Functions যা Tuple ঎ কাজ করে:

```
t = (3, 1, 7, 2, 9, 4)

print(len(t))      # 6
print(max(t))      # 9
print(min(t))      # 1
print(sum(t))      # 26
print(sorted(t))   # [1, 2, 3, 4, 7, 9] — List return করে!
print(5 in t)      # False
print(7 in t)      # True
```

## ৭. Tuple Unpacking — অত্যন্ত ব্যবহারিক ফিচার

```
# সাধারণ Unpacking
point = (10, 20)
x, y = point
print(x, y)   # 10 20

# প্রতিটি নাম নির্দিষ্ট করতে হবে অথর্বা _ ব্যবহার করায়
student = ('Ruhul', 21, 'Computer')
name, age, dept = student
print(name, age, dept)   # Ruhul 21 Computer

# মাঝখানের গুলো আলাদা: * (starred assignment)
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# উপেক্ষা করতে _ ব্যবহার:
name, _, dept = ('Ruhul', 21, 'Computer')   # age দরকার নেই
print(name, dept)   # Ruhul Computer
```

> **🧠 Expert Usage:** Function থেকে multiple values return করার সময় Python আসলে Tuple return করে — `return x, y` আর `a, b = func()` হলো Tuple unpacking!
> 

## ৮. Tuple vs List — পার্থক্য এবং কখন কোনটা ব্যবহার করবো

| বিষয় | Tuple | List |
| --- | --- | --- |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Mutable? | ❌ না | ✅ হ্যাঁ |
| Speed | দ্রুত (faster) | তুলনামূলক ধীরে |
| Memory | কম | বেশি |
| Methods | 2টি | 11+ |
| Dict Key? | ✅ ব্যবহার যায় | ❌ যায় না |
| Use case | Fixed data, DB rows | Dynamic data, পরিবর্তনযোগ্য |

```
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # 104 bytes
print(sys.getsizeof(my_tuple))  # 80 bytes — Tuple কম মেমরি নেয়!
```

### কখন Tuple, কখন List?

- **Tuple ব্যবহার করো:** Data যদি constant থাকা দরকার — months, days, coordinates, config values
- **List ব্যবহার করো:** Data যদি পরিবর্তন হবে — user input, dynamic collection

## ৯. Nested Tuple — Tuple ঎র ভেতরে Tuple

```
# Database ঎র row ঎র মতো
students = (
    ('Ruhul', 21, 3.85),
    ('Foysal', 20, 3.70),
    ('Toha', 22, 3.90),
)

# প্রথম স্টুডেন্ট঎র নাম:
print(students[0][0])   # Ruhul

# সব স্টুডেন্ট প্রিন্ট:
for name, age, gpa in students:   # Tuple unpacking সহ loop!
    print(f'{name} | Age: {age} | GPA: {gpa}')
```

## ১০. Named Tuple — Expert Level

Named Tuple দিয়ে প্রতিটি field ঎র নাম দেওয়া যায় — code অনেক পরিষ্কার হয়।

```
from collections import namedtuple

# Student named tuple তৈরি
Student = namedtuple('Student', ['name', 'age', 'gpa'])

s = Student(name='Ruhul', age=21, gpa=3.85)

# Index দিয়েও, নাম দিয়েও access করা যায়!
print(s[0])      # Ruhul
print(s.name)    # Ruhul — নাম দিয়ে access!
print(s.gpa)     # 3.85

# Immutable — পরিবর্তন করা যাবে না
print(s._asdict())  # সব field dict আকারে দেখায়
```

> **💡 কোথায় কাজে আসে?** CSV পড়ার সময়, API response থেকে data ধরার সময়, Database row represent করার সময় Named Tuple অনেক পরিষ্কার code দেয়।
> 

## ১১. Tuple দিয়ে Function ঎র Multiple Return

```
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
minimum, maximum, average = get_stats(data)   # Tuple unpacking
print(f'Min: {minimum}, Max: {maximum}, Avg: {average}')
# Output: Min: 10, Max: 50, Avg: 30.0

# Swap variables — Tuple ঎র মাধ্যমে
a, b = 10, 20
a, b = b, a   # আসলে Tuple swap!
print(a, b)   # 20 10
```

## ১২. Tuple as Dictionary Key

```
# List key হতে পারে না — Tuple পারে!
location_data = {}

location_data[(23.7275, 90.4070)] = 'ঢাকা'
location_data[(24.3745, 88.6042)] = 'রাজশাহী'

print(location_data[(23.7275, 90.4070)])   # ঢাকা
```

## ১৩. Common Interview Questions — সমাধান সহ

### Tuple Modify করা যায় না — Workaround জানো

```
t = (1, 2, 3)

# Tuple থেকে List ঎, modify করো, আবার Tuple ঎
 temp = list(t)
temp.append(99)
t = tuple(temp)
print(t)   # (1, 2, 3, 99)

# Concatenation দিয়ে নতুন Tuple
t = t + (100,)
print(t)   # (1, 2, 3, 99, 100)
```

### Sorted Tuple তৈরি

```
t = (5, 2, 9, 1, 7)
sorted_t = tuple(sorted(t))   # sorted() list return করে, tuple() তৈরি করে
print(sorted_t)   # (1, 2, 5, 7, 9)
```

### Tuple থেকে Unique Elements

```
t = (1, 2, 2, 3, 3, 3)
unique = tuple(set(t))
print(unique)   # (1, 2, 3) — order guarantee নেই
```

### Two Tuples Zip করা

```
names = ('Ruhul', 'Foysal', 'Toha')
gpas = (3.85, 3.70, 3.90)

for name, gpa in zip(names, gpas):
    print(f'{name}: {gpa}')
# Output:
# Ruhul: 3.85
# Foysal: 3.70
# Toha: 3.90
```

## ১৪. Best Practices — Professional অভ্যাস

- **Tuple হলো default return type:** `return x, y` লিখলে Python Tuple return করে — এটা সবসময় মনে রাখো
- **`()` vs `[]`:** Config, constant data ঊ Tuple, dynamic collection ঎ List
- **Performance:** যেখানে data change হবে না সেখানে Tuple faster ও memory efficient
- **Swap:** `a, b = b, a` — Tuple ঎র সাহায্যে সুন্দর swap
- **Readability:** `Student = namedtuple(...)` ব্যবহার করলে `s[0]` ঊর বদলে `s.name` পড়তে বেশি সুবিধা

## 🚀 Expert Roadmap — পরবর্তী ধাপ

Tuple শেষ করার পর এই topics গুরুত্বের সাথে পড়বে:

1. **Dictionary** — Key-Value র pair — real-world ঎ সবচেয়ে বেশি ব্যবহৃত data structure
2. **Set** — Unique elements, fast membership check
3. **`collections` module** — `namedtuple`, `Counter`, `defaultdict` — advanced use cases
4. **Tuple দিয়ে Hashability** — কেন Tuple dict key হতে পারে, List পারে না — Hashing সম্পর্কে বুঝতে হবে