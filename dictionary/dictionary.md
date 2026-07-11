# Python Dictionary — Data Structure

## ১. Dictionary কী এবং কেন ব্যবহার করি?

- **Definition:** Dictionary হলো একটি Mutable, Ordered Key-Value pair collection যা `{ }` curly braces এ তৈরি হয়। Key হলো index ঎র মতো — Key দিয়ে Value খুঁজে পাওয়া যায়।
- **Real-life Analogy:** জন্ম নোংদন (Contact Book) ঎র মতো — নাম (Key) দিয়ে ফোন নম্বর (Value) খুঁজে পাওয়া যায়।
- **কোথায় Dictionary ব্যবহার হয়?**
    - User profile, student record সংরক্ষণ
    - API response data পার্স করা (JSON)
    - Word frequency count
    - Configuration settings

## ২. Dictionary ঎র ৪ বৈশিষ্ট্য (Powers)

### ২.১ Mutable — Key-Value add/remove/change সম্ভব

### ২.২ Key Unique — একই Key দুইবার থাকতে পারে না, Value duplicate হতে পারে

### ২.৩ Ordered — Python 3.7+ ঊ insertion order মনে রাখে

### ২.৪ Heterogeneous — যেকোনো type ঎র Key ও Value রাখা যায়

```
student = {
    'name': 'Ruhul',
    'age': 21,
    'gpa': 3.85,
    'subjects': ['Math', 'CS', 'English'],
    'is_active': True
}
print(student['name'])   # Ruhul
```

## ৩. Dictionary তৈরি করা

```
# খালি Dictionary
empty = {}
empty2 = dict()

# সরাসরি
person = {'name': 'Ruhul', 'city': 'Rajshahi'}

# dict() constructor দিয়ে
person2 = dict(name='Ruhul', city='Rajshahi')

# Nested Dictionary
school = {
    'student1': {'name': 'Ruhul', 'gpa': 3.85},
    'student2': {'name': 'Foysal', 'gpa': 3.70}
}
print(school['student1']['name'])   # Ruhul

# fromkeys() — সব key ঊ একই default value
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}
```

## ৪. CRUD Operations — Create, Read, Update, Delete

```
student = {'name': 'Ruhul', 'age': 21}

# CREATE — নতুন Key-Value যোগ
student['dept'] = 'Computer'
print(student)   # {'name': 'Ruhul', 'age': 21, 'dept': 'Computer'}

# READ — Value পড়া
print(student['name'])          # Ruhul
print(student.get('gpa', 0.0))  # 0.0 — Key না থাকলে default ফেরায়

# UPDATE — মান বদলানো
student['age'] = 22
print(student['age'])   # 22

# DELETE — মুছে দেওয়া
removed = student.pop('dept')   # মুছে ও ফেরায়
del student['age']              # শুধু মুছে
```

> **⚠️ গুরুত্বপূর্ণ:** `student['gpa']` লিখলে Key না থাকলে `KeyError` দেবে। `student.get('gpa', 0.0)` ব্যবহার করো — Key না থাকলে default return করবে।
> 

## ৫. Dictionary Traversing — সব পদ্ধতি

```
student = {'name': 'Ruhul', 'age': 21, 'dept': 'Computer'}

# Method 1: Keys মাত্র (default)
for key in student:
    print(key)   # name, age, dept

# Method 2: .keys()
for key in student.keys():
    print(key)

# Method 3: .values()
for value in student.values():
    print(value)   # Ruhul, 21, Computer

# Method 4: .items() — Key ও Value একসাথে (Best Practice)
for key, value in student.items():
    print(f'{key}: {value}')
# Output:
# name: Ruhul
# age: 21
# dept: Computer
```

## ৬. Dictionary Methods — সর্বমোট

```
d = {'a': 1, 'b': 2, 'c': 3}

# .get(key, default) — safe access
print(d.get('a'))        # 1
print(d.get('z', 0))    # 0 — নেই, default 0

# .update() — অন্য dict মার্জ করা
d.update({'d': 4, 'a': 99})   # 'a' update, 'd' যোগ
print(d)  # {'a': 99, 'b': 2, 'c': 3, 'd': 4}

# .pop(key) — element মুছে value return
val = d.pop('d')
print(val)   # 4

# .popitem() — last item মুছে (key, value) tuple return
item = d.popitem()
print(item)   # ('c', 3)

# .setdefault() — Key না থাকলে default set করে
d.setdefault('x', 100)
print(d['x'])   # 100
d.setdefault('a', 999)   # 'a' আগে থেকেই আছে, change হবে না

# .keys(), .values(), .items()
print(list(d.keys()))    # সব key
print(list(d.values()))  # সব value
print(list(d.items()))   # সব (key, value) tuple

# .copy()
d2 = d.copy()

# .clear()
d3 = {'x': 1}
d3.clear()
print(d3)   # {}
```

| Method | কাজ |
| --- | --- |
| `get(k, default)` | Safe access — KeyError নেই |
| `update({...})` | অন্য dict merge / key update |
| `pop(k)` | element মুছে, value return |
| `popitem()` | last (key, value) মুছে, return |
| `setdefault(k, v)` | Key না থাকলে default set |
| `keys()` | সব key ঎র view |
| `values()` | সব value ঎র view |
| `items()` | সব (key, value) পেয়ার |
| `copy()` | Shallow copy |
| `clear()` | সব মুছে |

## ৭. Dictionary Comprehension — Expert Style

```
# Syntax: {key: value for item in iterable if condition}

numbers = [1, 2, 3, 4, 5]

# Square dictionary
squares = {n: n**2 for n in numbers}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Condition সহ
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)   # {2: 4, 4: 16}

# Key-Value swap
d = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in d.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}

# Word frequency count
sentence = 'the quick brown fox jumps over the lazy dog the'
freq = {word: sentence.split().count(word) for word in set(sentence.split())}
print(freq)
```

## ৮. Interview Questions — সমাধান সহ

### দুটি Dictionary Merge করা

```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# Method 1: update()
merged = d1.copy()
merged.update(d2)

# Method 2: ** unpacking (Python 3.5+)
merged = {**d1, **d2}
print(merged)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Method 3: | operator (Python 3.9+)
merged = d1 | d2
```

### Dictionary ঎র সব Values যোগ করা

```
d = {'a': 10, 'b': 20, 'c': 30}
total = sum(d.values())
print(total)   # 60
```

### Element Frequency Count

```
# Method 1: Manual
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# Method 2: collections.Counter (Expert)
from collections import Counter
freq = Counter(words)
print(freq)   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(freq.most_common(2))   # সবচেয়ে বেশি 2টি
```

### Common Keys ঎র Values যোগ করা

```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 10, 'c': 20, 'd': 30}

combined = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
print(combined)   # {'a': 1, 'b': 12, 'c': 23, 'd': 30}
```

### Value দিয়ে Sort করা

```
scores = {'Ruhul': 85, 'Foysal': 92, 'Toha': 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)   # {'Foysal': 92, 'Ruhul': 85, 'Toha': 78}
```

## ৯. Nested Dictionary

```
students = {
    'Ruhul':  {'age': 21, 'gpa': 3.85, 'dept': 'CS'},
    'Foysal': {'age': 20, 'gpa': 3.70, 'dept': 'EEE'},
}

# Access
print(students['Ruhul']['gpa'])   # 3.85

# Traverse
for name, info in students.items():
    print(f"{name}: GPA = {info['gpa']}")
```

## ১০. Best Practices

- **`dict.get()` সবসময় ব্যবহার করো** — `d['key']` KeyError দিতে পারে
- **`dict.items()` দিয়ে traverse** — `keys()` + `d[k]` ঎র চেয়ে দ্রুত
- **`collections.Counter`** — frequency count ঎র জন্য সবের সেরা টুল
- **`collections.defaultdict`** — missing key ঎র জন্য default value আপনা দেয়

```
from collections import defaultdict
dd = defaultdict(list)   # প্রতিটি missing key ঊ empty list default
dd['fruits'].append('apple')   # KeyError নেই!
print(dd)   # defaultdict(<class 'list'>, {'fruits': ['apple']})
```

## 🚀 Expert Roadmap

1. **`collections` module** — `Counter`, `defaultdict`, `OrderedDict`
2. **JSON** — Dictionary আর JSON আসলে একই জিনিস — API কাজে অপরিহার্য
3. **Hashing** — দ্রুত lookup ঊর কারণ O(1)
4. **Dictionary + OOP** — `__dict__` attribute এবং dataclasses