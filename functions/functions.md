# Python Functions

## ১. ফাংশনের মূল ধারণা (Core Intuition)

- **Definition:** ফাংশন হলো একটি নামযুক্ত কোডের ব্লক যা একটি নির্দিষ্ট কাজ করে। একবার লিখলে বারবার ব্যবহার করা যায় — শুধু নাম ধরে ডাকলেই হয়।
- **Real-life Analogy:** রান্নার রেসিপির মতো ভাবো। প্রতিবার ডাল রান্না করার সময় রেসিপি নতুন করে লিখতে হয় না — একবার লিখে রাখো, যখন দরকার ডাকো।
- **কেন ফাংশন?**
    - **DRY Principle:** Don't Repeat Yourself — একই কোড বারবার না লিখে ফাংশনে রাখো
    - **Modularity:** বড় প্রোগ্রামকে ছোট ছোট অংশে ভাগ করা যায়
    - **Readability:** কোড পড়তে ও বুঝতে সহজ হয়
    - **Easy Debugging:** সমস্যা হলে শুধু সেই ফাংশনটি ঠিক করলেই চলে
- **Built-in vs User-defined:**
    - **Built-in:** Python নিজেই দেয় — `print()`, `input()`, `len()`, `range()`, `type()`
    - **User-defined:** তুমি নিজে `def` দিয়ে বানাও

## ২. ফাংশন তৈরির Syntax ও Architecture

### 🛠️ Production-Ready Syntax:

```
def function_name(parameter1, parameter2):
    """Docstring: ফাংশনটা কী করে তার বর্ণনা (ঐচ্ছিক কিন্তু professional)"""
    # ফাংশনের body — কাজের কোড এখানে
    return value  # ঐচ্ছিক — result ফিরিয়ে দেওয়া

# ফাংশন call করা:
result = function_name(argument1, argument2)
```

### 🧠 Expert Developer Insights:

- **Naming Convention:** ফাংশনের নাম সবসময় `lowercase` এবং `underscore` দিয়ে লেখো — `calculate_tax()`, `get_user_name()` (PEP 8 style)
- **Single Responsibility:** একটি ফাংশন শুধু একটি কাজ করবে — এটাই Clean Code এর মূল নীতি
- **ফাংশন কল হওয়ার আগে শুধু define হয়** — Python ইন্টারপ্রেটার `def` দেখলে ফাংশনটি memory-তে রাখে কিন্তু চালায় না

```
# উদাহরণ:
def greet():
    print('স্বাগতম Python এ!')

greet()  # এখানে call করলে তবেই চলবে
```

## ৩. Parameters এবং Arguments — পার্থক্য জানো

- **Parameter:** ফাংশন `define` করার সময় যে variable রাখা হয় — এটি placeholder, বলে 'এখানে একটা মান আসবে'
- **Argument:** ফাংশন `call` করার সময় যে actual মান পাঠানো হয় — এটি real value

```
def greet(name):         # 'name' হলো PARAMETER
    print(f'Hello, {name}!')

greet('Ruhul')           # 'Ruhul' হলো ARGUMENT
# Output: Hello, Ruhul!
```

| বিষয় | Parameter | Argument |
| --- | --- | --- |
| কখন? | define করার সময় | call করার সময় |
| কী? | Variable (placeholder) | Actual value |
| উদাহরণ | `def func(x, y)` | `func(10, 20)` |

### 🚨 গুরুত্বপূর্ণ নিয়ম:

Parameter এবং Argument এর সংখ্যা অবশ্যই মিলতে হবে। তিনটি parameter থাকলে তিনটি argument দিতে হবে — না হলে `TypeError` আসবে।

## ৪. Arguments এর প্রকারভেদ (৫ ধরন)

### ৪.১ Positional Arguments — ক্রম অনুযায়ী

সবচেয়ে সাধারণ ধরন। যে ক্রমে দেবে, সেই ক্রমে parameter এ যাবে।

```
def introduce(name, city, age):
    print(f'আমি {name}, {city} থেকে, বয়স {age}')

introduce('রুহুল', 'রাজশাহী', 21)  # ক্রম গুরুত্বপূর্ণ!
# Output: আমি রুহুল, রাজশাহী থেকে, বয়স 21
```

> **⚠️ সতর্কতা:** ক্রম ভুল হলে ফলাফল ভুল হবে কিন্তু error নাও আসতে পারে!
> 

### ৪.২ Default Arguments — Default মান সহ

ফাংশন define করার সময় parameter এর একটি default মান দিয়ে রাখা যায়। call করার সময় সেই argument না দিলে default মান ব্যবহার হয়।

```
def greet(name, message='স্বাগতম!'):
    print(f'{name}, {message}')

greet('Ruhul')                # Output: Ruhul, স্বাগতম!
greet('Foysal', 'কেমন আছ?')  # Output: Foysal, কেমন আছ?
```

> **🚨 নিয়ম:** Default parameter গুলো সবসময় Non-default এর পরে রাখতে হবে।
> 

> ✅ `def func(a, b=10)` — সঠিক
> 

> ❌ `def func(a=10, b)` — এটি `SyntaxError` দেবে
> 

### ৪.৩ Keyword Arguments — নাম ধরে

নাম উল্লেখ করে argument পাঠানো হয়। এতে ক্রম যেকোনো হতে পারে।

```
def register(name, roll, department):
    print(f'{department} বিভাগে {name}, রোল: {roll}')

# Keyword argument — ক্রম মিলছে না, তবুও সঠিক কাজ করবে
register(roll='2301', department='Computer', name='Ruhul')
# Output: Computer বিভাগে Ruhul, রোল: 2301
```

### ৪.৪ *args — যেকোনো সংখ্যক Positional Arguments

যখন জানা থাকে না ফাংশনে কতটি argument আসবে। এটি সব argument গুলো একটি **Tuple** হিসেবে ধরে।

```
def sum_all(*numbers):    # numbers একটি tuple
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))         # Output: 6
print(sum_all(10, 20, 30, 40))  # Output: 100
print(sum_all(5))               # Output: 5
```

### ৪.৫ kwargs — যেকোনো সংখ্যক Keyword Arguments

`**kwargs` দিয়ে যেকোনো সংখ্যক keyword argument পাঠানো যায়। এটি সব argument গুলো একটি **Dictionary** হিসেবে ধরে।

```
def student_info(**details):   # details একটি dictionary
    for key, value in details.items():
        print(f'{key}: {value}')

student_info(name='Ruhul', roll='2301', dept='Computer', gpa=3.8)
# Output:
# name: Ruhul
# roll: 2301
# dept: Computer
# gpa: 3.8
```

### ৪.৬ সব ধরনের Argument একসাথে — সঠিক ক্রম

```
# সঠিক ক্রম: regular → *args → default → **kwargs
def mega_function(regular, *args, default='ok', **kwargs):
    print('Regular:', regular)
    print('Args Tuple:', args)
    print('Default:', default)
    print('Kwargs Dict:', kwargs)

mega_function('hello', 1, 2, 3, default='custom', x=10, y=20)
# Output:
# Regular: hello
# Args Tuple: (1, 2, 3)
# Default: custom
# Kwargs Dict: {'x': 10, 'y': 20}
```

## ৫. Return Statement — মান ফিরিয়ে আনা

- **`return`** statement দিয়ে ফাংশন একটি মান ফিরিয়ে দেয় যা সংরক্ষণ বা সরাসরি ব্যবহার করা যায়
- **`return` ছাড়া ফাংশন `None` ফিরিয়ে দেয়** — এটি অনেকে ভুলে যায়!

```
def add(a, b):
    return a + b

result = add(10, 20)     # result = 30
print(add(5, 3) * 2)     # return এর মান সরাসরি ব্যবহার → 16

# Multiple values return (Tuple হিসেবে ফেরে)
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 1, 7, 2, 9])
print(minimum, maximum)  # Output: 1 9
```

### 🧠 Early Return Pattern — Professional কোড লেখার অভ্যাস:

```
def divide(a, b):
    if b == 0:
        return None   # early return — nested if এড়ানো যায়
    return a / b
```

## ৬. Variable Scope — LEGB Rule

**Scope** মানে কোথায় থেকে একটি variable দেখা যাবে। Python এ **LEGB Rule** অনুসরণ করা হয়।

| Scope | মানে | উদাহরণ |
| --- | --- | --- |
| **L** — Local | ফাংশনের ভেতরে | `def func(): x = 10` |
| **E** — Enclosing | Nested ফাংশনের বাইরের ফাংশন | inner → outer |
| **G** — Global | Module level, সবার বাইরে | `count = 0` |
| **B** — Built-in | Python এর নিজস্ব | `len`, `print`, `range` |

```
count = 0   # Global variable

def increment():
    global count   # global keyword ছাড়া বাইরের variable পরিবর্তন হবে না
    count += 1

increment()
increment()
print(count)   # Output: 2

# nonlocal — Nested function এ
def outer():
    x = 10
    def inner():
        nonlocal x   # outer এর x পরিবর্তন করবো
        x = 20
    inner()
    print(x)   # Output: 20
```

> **⚠️ Expert Advice:** `global` variable বেশি ব্যবহার করা ভালো অভ্যাস নয়। যতটা সম্ভব `return` দিয়ে মান ফিরিয়ে আনো — Global state অনেক সময় bug এর কারণ হয়।
> 

## ৭. Lambda Functions — Anonymous Functions

`Lambda` হলো এক লাইনের নামহীন ফাংশন। যখন `def` দিয়ে পুরো ফাংশন লেখা অতিরিক্ত মনে হয়, তখন Lambda ব্যবহার হয়।

```
# Syntax: lambda parameter: expression

# সাধারণ ফাংশন vs Lambda
def square(x):
    return x * x

square = lambda x: x * x   # একই কাজ এক লাইনে
print(square(5))            # Output: 25

# Lambda এর বাস্তব ব্যবহার
numbers = [1, 2, 3, 4, 5, 6]

# map() — প্রতিটি element transform
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25, 36]

# filter() — condition মেনে চলা element বের করে
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # [2, 4, 6]

# sorted() — custom key দিয়ে sort
names = ['Ruhul', 'Foysal', 'Toha', 'Sadat']
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)  # ['Toha', 'Ruhul', 'Sadat', 'Foysal']
```

## ৮. Nested Functions ও Closure

- **Nested Function:** একটি ফাংশনের ভেতরে আরেকটি ফাংশন define করা
- **Closure:** Inner ফাংশন যখন Outer ফাংশনের variable মনে রাখে — এমনকি outer ফাংশন শেষ হয়ে গেলেও!

```
def make_counter(start=0):
    count = start   # এই variable টি closure 'মনে' রাখবে

    def counter():
        nonlocal count
        count += 1
        return count

    return counter   # function টি return করা হচ্ছে

counter1 = make_counter()    # counter1 এর নিজস্ব state
counter2 = make_counter(10)  # counter2 এর আলাদা state

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 11
print(counter1())  # 3 — counter1 আগের state মনে রেখেছে!
```

> **💡 Closure কোথায় কাজে আসে?** Decorator তৈরিতে, Callback function এ, Factory function এ — যেখানে state ধরে রাখতে হয়।
> 

## ৯. Higher-Order Functions

Python এ ফাংশন একটি **First-Class Object** — তাই:

- ফাংশনকে variable এ রাখা যায়
- ফাংশনকে অন্য ফাংশনের **argument** হিসেবে পাঠানো যায়
- ফাংশন থেকে ফাংশন **return** করা যায়

```
def apply_twice(func, value):
    return func(func(value))   # func কে argument হিসেবে নিচ্ছে

def double(x):
    return x * 2

result = apply_twice(double, 3)   # double(double(3)) = double(6) = 12
print(result)  # 12

# reduce() — সব element মিলিয়ে একটি মান
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)  # 1×2×3×4×5
print(product)  # 120
```

## ১০. Decorators — ফাংশনকে সুপারচার্জ করা

**Decorator** হলো এমন একটি ফাংশন যা অন্য একটি ফাংশনকে wrap করে — original code না বদলে তার আগে বা পরে কিছু কোড চালায়।

```
import time

def timer(func):   # Decorator ফাংশন
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # original ফাংশন চালানো
        end = time.time()
        print(f'{func.__name__} সময় নিলো: {end - start:.4f} সেকেন্ড')
        return result
    return wrapper

@timer   # এটি: slow_function = timer(slow_function) এর সমতুল্য
def slow_function():
    time.sleep(1)
    print('কাজ শেষ!')

slow_function()
# Output:
# কাজ শেষ!
# slow_function সময় নিলো: 1.0012 সেকেন্ড
```

> **💡 Real-world Usage:** Logging, Authentication check, Rate limiting, Caching — এই সব কাজে Decorator ব্যবহার হয়।
> 

## ১১. Recursion — ফাংশন নিজেকে নিজে ডাকে

Recursion হলো যখন একটি ফাংশন নিজেকে নিজে call করে। প্রতিটি recursive ফাংশনে অবশ্যই:

1. **Base Case:** কখন থামতে হবে — এটি ছাড়া অনন্তকাল চলবে!
2. **Recursive Case:** নিজেকে ছোট ইনপুট দিয়ে call করা

```
# Factorial: n! = n × (n-1)!
def factorial(n):
    if n == 0:              # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))   # 5×4×3×2×1 = 120

# Fibonacci
def fibonacci(n):
    if n <= 1:            # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)   # Recursive case

for i in range(8):
    print(fibonacci(i), end=' ')
# Output: 0 1 1 2 3 5 8 13
```

> **⚠️ সতর্কতা:** Python এ default recursion limit হলো **1000**। খুব গভীর recursion এ `RecursionError` আসে। বড় সমস্যায় loop ব্যবহার করাই নিরাপদ।
> 

## ১২. Best Practices — Professional Python Developer এর অভ্যাস

### Docstring লেখো:

```
def calculate_bmi(weight_kg, height_m):
    """
    BMI হিসাব করে।

    Args:
        weight_kg (float): কেজিতে ওজন
        height_m (float): মিটারে উচ্চতা

    Returns:
        float: BMI মান
    """
    return weight_kg / (height_m ** 2)
```

### Type Hints ব্যবহার করো:

```
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, times: int = 1) -> str:
    return (f'Hello, {name}! ' * times).strip()
```

### সাধারণ ভুল ও সমাধান:

| ভুল | সমাধান |
| --- | --- |
| `def func(lst=[])` — Mutable default | `def func(lst=None): if lst is None: lst = []` |
| Global variable বেশি ব্যবহার | Parameter ও return ব্যবহার করো |
| অস্পষ্ট নাম: `def f()`, `def do()` | বর্ণনামূলক: `def calculate_area()` |
| Recursion এ base case ভুলে যাওয়া | সবসময় base case আগে লেখো |

## 🚀 এক্সপার্ট রোডম্যাপ — পরবর্তী ধাপ:

Functions শেষ করার পর এই টপিকগুলো গুরুত্বের সাথে পড়বে:

1. **Generators ও `yield`** — মেমরি-efficient ফাংশন লেখার জন্য
2. **`functools` module** — `partial()`, `lru_cache()`, `wraps()` — professional decorating এর জন্য
3. **`*` এবং `/` parameter separators** — Python 3.8+ এ keyword-only ও positional-only argument enforce করতে
4. **Async Functions (`async def`, `await`)** — Non-blocking code লেখার জন্য, যা modern web backend এ অপরিহার্য
5. **Testing Functions** — `pytest` বা `unittest` দিয়ে নিজের ফাংশন test করা শেখো