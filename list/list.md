# Python List — Data Structure

## ১. Data Structures — মূল ধারণা

- **Data Structure কী?** Data structure হলো data সংরক্ষণ, সাজানো এবং দক্ষতার সাথে ব্যবহার করার একটি পদ্ধতি। সঠিক data structure বেছে নিলে program অনেক দ্রুত ও মেমরি-efficient হয়।
- **Python এ মোট ৪টি In-built Data Structure আছে:**
    1. **List** — Mutable, Ordered, Duplicates অনুমোদিত
    2. **Tuple** — Immutable (পরিবর্তন করা যায় না), Ordered
    3. **Dictionary** — Key-Value pair, Unordered (Python 3.7+ এ insertion order মনে রাখে)
    4. **Set** — Unordered, Duplicates নেই
- **Custom Data Structures:** Stack, Queue, Linked List, Graph, Tree — এগুলো In-built দিয়ে তৈরি করতে হয়। DSA (Data Structures & Algorithms) পরে আলাদাভাবে শিখতে হবে।

| Data Structure | Mutable? | Ordered? | Duplicates? | Syntax |
| --- | --- | --- | --- | --- |
| **List** | ✅ হ্যাঁ | ✅ হ্যাঁ | ✅ হ্যাঁ | `[1, 2, 3]` |
| **Tuple** | ❌ না | ✅ হ্যাঁ | ✅ হ্যাঁ | `(1, 2, 3)` |
| **Dictionary** | ✅ হ্যাঁ | ✅ হ্যাঁ | Key: ❌ | `{'a': 1}` |
| **Set** | ✅ হ্যাঁ | ❌ না | ❌ না | `{1, 2, 3}` |

## ২. List — চারটি মূল বৈশিষ্ট্য (Powers)

### ২.১ Mutable — পরিবর্তনযোগ্য

List তৈরির পরেও তার element যোগ, বিয়োগ বা পরিবর্তন করা যায়। String এ এটি সম্ভব না।

```
numbers = [10, 20, 30]
numbers[1] = 99          # index 1 এর মান বদলানো হলো
print(numbers)           # Output: [10, 99, 30]
```

### ২.২ Duplicates — একই মান বারবার রাখা যায়

```
marks = [85, 90, 85, 72, 90]
print(marks)   # Output: [85, 90, 85, 72, 90] — duplicate আছে, কোনো সমস্যা নেই
```

### ২.৩ Ordered — ক্রম বজায় থাকে

List এ element যে ক্রমে রাখা হয়, সেই ক্রমই বজায় থাকে। Index দিয়ে নির্দিষ্ট position এর element পাওয়া যায়।

### ২.৪ Heterogeneous — মিশ্র data type

```
mixed = [42, 'Ruhul', 3.14, True, [1, 2]]   # এক List এ সব ধরনের data!
print(mixed)
# Output: [42, 'Ruhul', 3.14, True, [1, 2]]
```

## ৩. List তৈরি করা (Creation)

```
# খালি List
empty = []
empty2 = list()

# সরাসরি তৈরি
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]

# range() থেকে List
evens = list(range(0, 11, 2))   # [0, 2, 4, 6, 8, 10]

# String থেকে List
letters = list('Ruhul')         # ['R', 'u', 'h', 'u', 'l']

# Nested List (Matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # Output: 6 — 2nd row, 3rd column
```

## ৪. Indexing ও Slicing

List indexing string এর মতোই কাজ করে।

```
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
#           0         1         2         3        4
#          -5        -4        -3        -2       -1

# Positive Index
print(fruits[0])    # apple
print(fruits[3])    # mango

# Negative Index (শেষ থেকে গণনা)
print(fruits[-1])   # grape
print(fruits[-2])   # mango

# Slicing: list[start:stop:step]
print(fruits[1:4])    # ['banana', 'cherry', 'mango']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'mango', 'grape']
print(fruits[::2])    # ['apple', 'cherry', 'grape'] — একটি পরপর
print(fruits[::-1])   # Reverse — ['grape', 'mango', 'cherry', 'banana', 'apple']
```

> **🧠 Expert Insight:** Slicing একটি নতুন List তৈরি করে —
>  original List অপরিবর্তিত থাকে। এটি `copy()` এর মতোই কাজ করে।
> 

## ৫. List Traversing (Loop দিয়ে)

```
fruits = ['apple', 'banana', 'cherry']

# Method 1: সরাসরি element ধরে (Best Practice)
for fruit in fruits:
    print(fruit)

# Method 2: Index ধরে
for i in range(len(fruits)):
    print(f'Index {i}: {fruits[i]}')

# Method 3: enumerate() — index ও element একসাথে (Expert style)
for index, fruit in enumerate(fruits):
    print(f'{index} -> {fruit}')

# Output (enumerate):
# 0 -> apple
# 1 -> banana
# 2 -> cherry

# While loop দিয়ে
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

## ৬. List এর সব Methods — বিস্তারিত

```
numbers = [5, 2, 9, 1, 5, 6]   # Initial list
```

| Method | কাজ | উদাহরণ |  |
| --- | --- | --- | --- |
| `append(x)` | শেষে একটি element যোগ | `numbers.append(10)` |  |
| `insert(i, x)` | নির্দিষ্ট index এ element যোগ | `numbers.insert(2, 15)` |  |
| `extend([...])` | অন্য List এর সব element যোগ | `numbers.extend([20, 25])` |  |
| `remove(x)` | প্রথম occurrence মুছে দেয় | `numbers.remove(5)` |  |
| `pop(i)` | নির্দিষ্ট index এর element মুছে ও ফেরায় | `numbers.pop(3)` |  |
| `index(x)` | প্রথম occurrence এর index বলে | `numbers.index(6)` |  |
| `count(x)` | কতবার আছে গণনা করে | `numbers.count(5)` |  |
| `sort()` | ascending order এ sort করে | `numbers.sort()` |  |
| `sort(reverse=True)` | descending order এ sort করে | `numbers.sort(reverse=True)` |  |
| `reverse()` | List উল্টে দেয় | `numbers.reverse()` |  |
| `copy()` | List এর একটি copy তৈরি করে | `new = numbers.copy()` |  |
| `clear()` | সব element মুছে দেয় | `numbers.clear()` |  |

```
numbers = [5, 2, 9, 1, 5, 6]

numbers.append(10)           # [5, 2, 9, 1, 5, 6, 10]
numbers.insert(2, 15)        # [5, 2, 15, 9, 1, 5, 6, 10]
numbers.extend([20, 25, 30]) # [5, 2, 15, 9, 1, 5, 6, 10, 20, 25, 30]
numbers.remove(5)            # প্রথম 5 মুছবে
popped_item = numbers.pop(3) # index 3 এর element মুছে সংরক্ষণ
index = numbers.index(6)     # 6 কোন index এ আছে
count_5 = numbers.count(5)   # 5 কতবার আছে
numbers.sort()               # Ascending sort
numbers.reverse()            # Reverse
new_numbers = numbers.copy() # Copy তৈরি
```

### ⚠️ append() vs extend() vs insert() — পার্থক্য জানা দরকার:

```
a = [1, 2, 3]

a.append([4, 5])    # [1, 2, 3, [4, 5]]   — পুরো list টাই একটি element হিসেবে যোগ
a = [1, 2, 3]
a.extend([4, 5])    # [1, 2, 3, 4, 5]    — element গুলো আলাদাভাবে যোগ
a = [1, 2, 3]
a.insert(1, 99)     # [1, 99, 2, 3]      — নির্দিষ্ট position এ যোগ
```

## ৭. Built-in Functions — List এর সাথে

```
numbers = [3, 1, 7, 2, 9, 4]

print(len(numbers))    # 6 — মোট element সংখ্যা
print(max(numbers))    # 9 — সর্বোচ্চ মান
print(min(numbers))    # 1 — সর্বনিম্ন মান
print(sum(numbers))    # 26 — সব মানের যোগফল
print(sorted(numbers)) # [1, 2, 3, 4, 7, 9] — নতুন sorted list (original অপরিবর্তিত)
print(list(reversed(numbers)))  # [4, 9, 2, 7, 1, 3]
print(5 in numbers)    # False — membership check
print(7 in numbers)    # True
```

## ৮. List Comprehension — Expert Style

List comprehension হলো এক লাইনে for loop চালিয়ে List তৈরির পদ্ধতি। এটি সাধারণ loop এর চেয়ে দ্রুত ও Pythonic।

```
# Syntax: [expression for item in iterable if condition]

# সাধারণ loop vs List Comprehension
# সাধারণ পদ্ধতি:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List Comprehension:
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# Condition সহ:
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10]

# String থেকে:
upper_fruits = [fruit.upper() for fruit in ['apple', 'banana', 'cherry']]
print(upper_fruits)   # ['APPLE', 'BANANA', 'CHERRY']

# Nested List Comprehension (Matrix flatten):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> **🧠 Expert Advice:** List Comprehension দ্রুত কিন্তু জটিল logic এর জন্য সাধারণ loop ব্যবহার করো — পড়তে সহজ হওয়া বেশি গুরুত্বপূর্ণ।
> 

## ৯. Nested List — 2D Matrix

```
# 3x3 Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access: matrix[row][column]
print(matrix[0][0])   # 1 — প্রথম row, প্রথম column
print(matrix[1][2])   # 6 — দ্বিতীয় row, তৃতীয় column
print(matrix[2][1])   # 8

# Matrix traverse
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()   # নতুন line
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Nested List Comprehension দিয়ে Matrix তৈরি:
zeros = [[0] * 3 for _ in range(3)]   # 3x3 zero matrix
print(zeros)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

## ১০. Common Interview Questions — সমাধান সহ

### ১০.১ Positive ও Negative elements আলাদা করা

```
numbers = [3, -1, 7, -5, 2, -8, 9, 0]

positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]

print('Positive:', positives)  # [3, 7, 2, 9]
print('Negative:', negatives)  # [-1, -5, -8]
```

### ১০.২ List এর Mean (গড়) বের করা

```
numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
print(f'Mean: {mean}')   # Mean: 30.0
```

### ১০.৩ সর্বোচ্চ element ও তার index

```
numbers = [3, 1, 7, 2, 9, 4]

greatest = max(numbers)
greatest_index = numbers.index(max(numbers))
print(f'Greatest: {greatest}, Index: {greatest_index}')   # Greatest: 9, Index: 4

# সব বড় element এর index (duplicates থাকলে):
all_max_indices = [i for i, x in enumerate(numbers) if x == max(numbers)]
print('All max indices:', all_max_indices)
```

### ১০.৪ দ্বিতীয় সর্বোচ্চ element

```
numbers = [3, 1, 7, 2, 9, 4]

# Method 1: sort করে
unique_sorted = sorted(set(numbers), reverse=True)
print('2nd Greatest:', unique_sorted[1])   # 7

# Method 2: max ছাড়া বাকিদের মধ্যে max
first_max = max(numbers)
second_max = max(x for x in numbers if x != first_max)
print('2nd Greatest:', second_max)   # 7
```

### ১০.৫ List sorted আছে কিনা চেক করা

```
def is_sorted(lst):
    # প্রতিটি element তার পরেরটির চেয়ে ছোট বা সমান কিনা
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(is_sorted([1, 2, 3, 4, 5]))   # True
print(is_sorted([1, 3, 2, 4, 5]))   # False
print(is_sorted([5, 4, 3, 2, 1]))   # False

# Descending sorted check:
print(sorted([1, 2, 3]) == [1, 2, 3])              # True — ascending?
print(sorted([5, 4, 3], reverse=True) == [5, 4, 3]) # True — descending?
```

### ১০.৬ আরও কিছু গুরুত্বপূর্ণ প্রশ্ন

```
numbers = [5, 2, 9, 1, 5, 6, 3, 7, 5]

# Duplicates বের করা
duplicates = [x for x in set(numbers) if numbers.count(x) > 1]
print('Duplicates:', duplicates)   # [5]

# Unique elements বের করা
unique = list(set(numbers))
print('Unique:', sorted(unique))   # [1, 2, 3, 5, 6, 7, 9]

# List reverse (copy)
reversed_list = numbers[::-1]
print('Reversed:', reversed_list)

# দুটি List merge ও sort
a = [3, 1, 7]
b = [4, 2, 8]
merged = sorted(a + b)
print('Merged & Sorted:', merged)   # [1, 2, 3, 4, 7, 8]
```

## ১১. Copy এর ফাঁদ — Shallow vs Deep Copy

```
# ⚠️ সরাসরি assign করলে same object reference হয়!
a = [1, 2, 3]
b = a          # b, a কে point করছে — একটি পরিবর্তন হলে দুটোই হবে!
b.append(99)
print(a)       # [1, 2, 3, 99] — a ও বদলে গেছে!

# ✅ সঠিক পদ্ধতি — copy() বা slicing
a = [1, 2, 3]
b = a.copy()   # অথবা b = a[:]
b.append(99)
print(a)       # [1, 2, 3] — a অপরিবর্তিত
print(b)       # [1, 2, 3, 99]

# ⚠️ Nested List এ copy() যথেষ্ট না — Deep Copy দরকার
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)
deep_copy[0][0] = 99
print(nested)     # [[1, 2], [3, 4]] — অপরিবর্তিত!
```

## ১২. Best Practices — Expert Python Developer এর অভ্যাস

- **`append()` vs `+` operator:** `a.append(x)` ব্যবহার করো — `a = a + [x]` প্রতিবার নতুন list তৈরি করে, বেশি মেমরি খরচ হয়
- **List Comprehension বনাম `map()`:** Pythonic code এ comprehension prefer করা হয়
- **`in` operator দিয়ে membership check:** `if x in my_list` — সহজ ও readable
- **`enumerate()` ব্যবহার করো:** `range(len(lst))` এর বদলে `enumerate(lst)` — বেশি Pythonic
- **Sorting:** `sorted()` original list অপরিবর্তিত রাখে, `sort()` in-place কাজ করে — পরিস্থিতি বুঝে ব্যবহার করো

```
# ❌ Un-Pythonic:
for i in range(len(fruits)):
    print(fruits[i])

# ✅ Pythonic:
for fruit in fruits:
    print(fruit)

# ✅ Index দরকার হলে:
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## 🚀 Expert Roadmap — পরবর্তী ধাপ

List শেষ করার পর এই topics গুরুত্বের সাথে পড়বে:

1. **Tuple** — Immutable List, কোথায় List এর বদলে Tuple ব্যবহার করতে হয়
2. **Dictionary** — Key-Value pair, real-world এ সবচেয়ে বেশি ব্যবহৃত
3. **Set** — Unique values, fast membership check
4. **Stack ও Queue** — List দিয়ে implement করা
5. **Time Complexity** — `append()` O(1), `insert()` O(n), `in` operator O(n) — এটা জানা job interview এ গুরুত্বপূর্ণ