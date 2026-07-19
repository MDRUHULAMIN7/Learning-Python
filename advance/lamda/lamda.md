## ১. Lambda কী?

- **Lambda** হলো `def` keyword ছাড়া এক লাইনের anonymous (নামহীন) function।
- ছোট, একবার ব্যবহারযোগ্য function এর জন্য আদর্শ।
- Multiple arguments নেওয়া যায়, কিন্তু **expression একটাই**।

## ২. Syntax ও Basic Example

```
# Syntax: lambda arguments: expression

# সাধারণ function vs Lambda
def square(x):
    return x ** 2

square = lambda x: x ** 2   # একই কাজ
print(square(4))   # Output: 16

# Multiple arguments
add = lambda x, y: x + y
print(add(3, 5))   # 8

# If-Else expression
check_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(check_even(7))   # Output: Odd
```

## ৩. Lambda এর বাস্তব ব্যবহার

```
# sorted() এ custom key
students = [('Ruhul', 3.85), ('Foysal', 3.70), ('Toha', 3.90)]
sorted_by_gpa = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_by_gpa)
# [('Toha', 3.90), ('Ruhul', 3.85), ('Foysal', 3.70)]

# map() এ
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10]

# filter() এ
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4]
```

## ৪. Lambda কখন ব্যবহার করবে, কখন নয়

| Lambda ভালো | def ভালো |
| --- | --- |
| Short, one-time use | Multiple lines দরকার |
| map/filter/sorted এর key | Reuse করবে |
| Readable থাকলে | Complex logic আছে |

> **⚠️ PEP 8:** Lambda কে variable এ assign না করাই ভালো — সেক্ষেত্রে `def` ব্যবহার করো।
>

## ১. Map

Python-এ map() হলো built-in function।

এটি যেকোনো iterable (list, tuple, set, string ইত্যাদি) নিয়ে কাজ করতে পারে।

map(func, iterable) প্রত্যেক item-এ func apply করে একটা iterator দেয়।

যদি আপনি list চান, তাহলে list(map(...)) করতে হয়।

JavaScript-এ map() হলো array এর method।

সেটা শুধু array-এ কাজ করে।

প্রতিটি element-এ callback চালায় এবং একটা নতুন array রিটার্ন করে।

সঠিক ভাষা
Python map direct list দেয় না; এটা lazy iterator দেয়।
JS map সরাসরি নতুন array দেয়।

- প্রতিটি item এ একটি function apply করে নতুন sequence তৈরি করে।
- Python 3 এ map object return করে — `list()` দিয়ে convert করতে হয়।
- Item skip বা remove করে না (সেটা filter এর কাজ)।

```
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))   # [2, 4, 6, 8]

# Normal function দিয়েও:
def square(x):
    return x ** 2

result = list(map(square, numbers))
print(result)   # [1, 4, 9, 16]

# Multiple iterables:
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]
```

## ২. Filter

- Condition পাস করা items রাখে, বাকি বাদ দেয়।
- Function `True` return করলে item রাখা হয়।

```
# Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))   # [2, 4]

# Positive numbers:
nums = [-3, -1, 0, 2, 5, -2, 8]
positives = list(filter(lambda x: x > 0, nums))
print(positives)   # [2, 5, 8]

# None দিলে Falsy values বাদ যায়:
data = [0, 1, '', 'hello', None, [], [1, 2]]
clean = list(filter(None, data))
print(clean)   # [1, 'hello', [1, 2]]
```

## ৩. Zip

- একাধিক iterable একসাথে pair করে tuple তৈরি করে।
- সবচেয়ে ছোট iterable এ পৌঁছালে থেমে যায়।

```
# Syntax: zip(iterable1, iterable2, ...)

names = ['Ruhul', 'Foysal', 'Toha']
gpas  = [3.85, 3.70, 3.90]
rolls = ['2301', '2302', '2303']

# দুটো pair:
for name, gpa in zip(names, gpas):
    print(f'{name}: {gpa}')
# Ruhul: 3.85
# Foysal: 3.70
# Toha: 3.90

# তিনটো pair:
for name, gpa, roll in zip(names, gpas, rolls):
    print(f'[{roll}] {name} — {gpa}')

# Dict তৈরি করতে:
student_dict = dict(zip(names, gpas))
print(student_dict)   # {'Ruhul': 3.85, 'Foysal': 3.70, 'Toha': 3.90}

# Unzip করতে:
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
print(nums)     # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

## ৪. Map vs Filter vs List Comprehension

|  | map() | filter() | Comprehension |
| --- | --- | --- | --- |
| কাজ | Transform | Filter | দুটোই |
| Return | map object | filter object | list/dict/set |
| Pythonic? | কম | কম | বেশি |

```
numbers = [1, 2, 3, 4, 5, 6]

# Equivalent expressions:
# map:
doubled_m = list(map(lambda x: x*2, numbers))
# comprehension:
doubled_c = [x*2 for x in numbers]

# filter:
evens_f = list(filter(lambda x: x%2==0, numbers))
# comprehension:
evens_c = [x for x in numbers if x%2==0]

# map + filter combined:
even_squares = list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))
# comprehension (আরো সহজ):
even_squares_c = [x**2 for x in numbers if x%2==0]
print(even_squares_c)   # [4, 16, 36]
```

# Modules & Packages

## ১. Module কী?

- **Module** হলো একটি single Python file (`.py`) যাতে functions, variables, বা classes থাকে।
- এক file এর code অন্য file এ `import` করে ব্যবহার করা যায়।
- Code organize ও reuse করার জন্য।

```
# Built-in module ব্যবহার:
import math
print(math.sqrt(16))   # Output: 4.0
print(math.pi)         # 3.141592653589793

import random
print(random.randint(1, 100))   # 1-100 এর মধ্যে random

import datetime
now = datetime.datetime.now()
print(now)   # বর্তমান তারিখ ও সময়
```

## ২. Import পদ্ধতি

```
# পুরো module import
import math
math.sqrt(25)   # module name দিয়ে access

# নির্দিষ্ট function import
from math import sqrt, pi
sqrt(25)   # সরাসরি ব্যবহার

# Alias দিয়ে import
import numpy as np   # third-party
import pandas as pd

# সব import (avoid করা ভালো)
from math import *
```

## ৩. নিজের Module তৈরি

```
# mymodule.py ফাইলে:
def greet(name):
    return f'Hello, {name}!'

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

# অন্য ফাইলে ব্যবহার:
import mymodule
print(mymodule.greet('Ruhul'))   # Hello, Ruhul!
print(mymodule.PI)               # 3.14159

from mymodule import greet, Calculator
print(greet('Foysal'))   # Hello, Foysal!
```

## ৪. Package কী?

- **Package** হলো একটি folder যাতে একাধিক module (Python files) থাকে।
- Sub-packages ও থাকতে পারে।
- `from` ও `import` keyword দিয়ে ব্যবহার করা যায়।

```
# Package structure:
# mypackage/
#   __init__.py
#   math_utils.py
#   string_utils.py

# ব্যবহার:
from mypackage import math_utils
from mypackage.string_utils import capitalize
```

## ৫. Popular Built-in Modules

| Module | কাজ | উদাহরণ |
| --- | --- | --- |
| `math` | Math operations | `math.sqrt()`, `math.pi` |
| `random` | Random number | `random.randint()` |
| `datetime` | Date & time | `datetime.now()` |
| `os` | File system | `os.path.exists()` |
| `json` | JSON parse/write | `json.loads()`, `json.dumps()` |
| `re` | Regex | `re.findall()` |
| `sys` | System info | `sys.argv`, `sys.exit()` |
| `collections` | Advanced DS | `Counter`, `defaultdict` |

## ৬. Third-party Packages (pip দিয়ে install)

```
# Terminal এ install:
pip install numpy
pip install pandas
pip install matplotlib

# ব্যবহার:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)   # [2 4 6 8 10]
```

## ৭. `if __name__ == '__main__'`

```
# mymodule.py:
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    # এই block শুধু এই file সরাসরি run করলে চলবে
    # import করলে চলবে না
    print(greet('Ruhul'))
```

> **💡 কেন দরকার?** Module হিসেবে import করলে test code না চালানোর জন্য এই pattern ব্যবহার হয়।
>