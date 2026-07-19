# Decorator

## ১. Decorator কী?

* **Decorator** হলো এমন একটি Function, যা অন্য একটি Function বা Method-এর **Behavior পরিবর্তন বা সম্প্রসারণ (Extend)** করে, কিন্তু মূল Function-এর Code পরিবর্তন করে না।
* সহজভাবে বলতে গেলে, **Decorator একটি Function-কে Wrap করে তার আগে বা পরে অতিরিক্ত কাজ করার সুযোগ দেয়।**
* **Real-life Analogy:** একটি Cake-এর ওপর Icing লাগানোর মতো। Cake (Function) একই থাকে, শুধু উপরে নতুন Feature যোগ হয়।
* 
decorator হলো একটি function যা অন্য একটা function নিয়ে কাজ করে।
সে মূল function-এর আগে বা পরে বা চারপাশে extra code চালাতে পারে।
@decorator_name syntax দিয়ে মূল function কে “wrap” করা হয়।
মূল function-এর কোড পরিবর্তন না করেই behavior যোগ করা যায়।

Decorator তৈরি করতে সাধারণত তিনটি ধাপ অনুসরণ করা হয়—

1. একটি **Outer Function (Decorator)** তৈরি করা।
2. এর ভেতরে একটি **Wrapper Function** তৈরি করা।
3. শেষে `wrapper` Function Return করা।

---

# ২. Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something before the Function runs.")

        func()

        print("Something after the Function runs.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()

# Output:
# Something before the Function runs.
# Hello!
# Something after the Function runs.
```

> **💡 `@my_decorator`-এর অর্থ:**
> `say_hello = my_decorator(say_hello)`
> অর্থাৎ `say_hello()` Function-কে `my_decorator()`-এর মাধ্যমে Wrap করা হয়েছে।

---

# ৩. Decorator ছাড়া Manual পদ্ধতি

Decorator Syntax (`@`) ব্যবহার না করেও একই কাজ করা যায়।

```python
def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)

say_hello()

# Output:
# Something before the Function runs.
# Hello!
# Something after the Function runs.
```

---

# ৪. `*args` ও `**kwargs` সহ Decorator

যদি Decorator-কে যেকোনো সংখ্যক Positional এবং Keyword Argument Support করাতে চাও, তাহলে `*args` এবং `**kwargs` ব্যবহার করতে হবে।

```python
def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(3, 5))

# Output:
# Before
# After
# 8
```

> **💡 Tip:** প্রায় সব Professional Decorator-এ `*args` এবং `**kwargs` ব্যবহার করা হয়, যাতে যেকোনো ধরনের Function-এর সাথে কাজ করা যায়।

---

# ৫. Real-world Decorators

## Timer Decorator

কোনো Function Execute হতে কত সময় লাগে, তা মাপার জন্য ব্যবহার করা হয়।

```python
import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__} সময় নিয়েছে: {end - start:.4f} সেকেন্ড")

        return result

    return wrapper


@timer
def slow_task():
    time.sleep(1)
    print("কাজ শেষ!")


slow_task()

# Output:
# কাজ শেষ!
# slow_task সময় নিয়েছে: 1.00xx সেকেন্ড
```

---

## Logger Decorator

Function Call হওয়ার আগে ও পরে Logging করার জন্য ব্যবহৃত হয়।

```python
def logger(func):

    def wrapper(*args, **kwargs):

        print(f"[LOG] {func.__name__} Call হয়েছে | Args: {args}")

        result = func(*args, **kwargs)

        print(f"[LOG] {func.__name__} শেষ হয়েছে | Result: {result}")

        return result

    return wrapper


@logger
def multiply(a, b):
    return a * b


multiply(4, 5)

# Output:
# [LOG] multiply Call হয়েছে | Args: (4, 5)
# [LOG] multiply শেষ হয়েছে | Result: 20
```

---

# ৬. Multiple Decorators

একটি Function-এর ওপর একাধিক Decorator ব্যবহার করা যায়।

```python
@decorator1
@decorator2
def my_func():
    pass
```

উপরের Code-এর প্রকৃত অর্থ হলো—

```python
my_func = decorator1(decorator2(my_func))
```

> **💡 মনে রাখবে:** নিচের Decorator (`decorator2`) আগে Apply হয়, তারপর উপরের Decorator (`decorator1`) Apply হয়।

---

# ৭. `functools.wraps` — Decorator-এর Best Practice

Decorator ব্যবহার করলে মূল Function-এর `__name__`, `__doc__` ইত্যাদি Metadata হারিয়ে যায়।

এটি ঠিক রাখতে `functools.wraps` ব্যবহার করা হয়।

```python
from functools import wraps


def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")

        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    """নাম ব্যবহার করে Greeting দেয়।"""

    print(f"Hello, {name}!")


print(greet.__name__)

# Output:
# greet
```

`@wraps` ব্যবহার না করলে Output হতো—

```python
wrapper
```

---

# সারসংক্ষেপ

| Topic               | কী শেখা হলো                                                  |
| ------------------- | ------------------------------------------------------------ |
| Decorator           | Function-এর Behavior পরিবর্তন বা সম্প্রসারণ করার Technique   |
| Wrapper Function    | মূল Function-কে Wrap করে অতিরিক্ত কাজ করে                    |
| `@decorator`        | `function = decorator(function)`-এর Shortcut Syntax          |
| `*args`, `**kwargs` | যেকোনো ধরনের Argument Support করার জন্য ব্যবহৃত হয়          |
| Timer Decorator     | Function-এর Execution Time মাপতে ব্যবহৃত হয়                 |
| Logger Decorator    | Function Call ও Result Log করার জন্য ব্যবহৃত হয়             |
| Multiple Decorators | একাধিক Decorator একসাথে ব্যবহার করা যায়                     |
| `functools.wraps`   | মূল Function-এর Metadata (`__name__`, `__doc__`) সংরক্ষণ করে |

