Data Types in Python

- **Data types** are the things we store in Variables and it defines what data type variables are.
- Python has built-in data types for different kinds of data.

## 🔢 Numbers

- **Integer (`int`):** All the numbers excluding decimal places and fraction. (e.g., `x = 5`, `y = -10`)
- **Float (`float`):** All the decimal numbers and fraction values are Float. (e.g., `pi = 3.14`, `price = 99.99`)
- **Complex (`complex`):** Numbers with real and imaginary parts are complex. In Python, it is written with a `j` as the imaginary part. (e.g., `z = 2 + 3j`)

## 🔤 Strings

- **Strings (`str`):** This is used to store anything in python, literally anything that are available on your keyboard.
- You have to use quotes to store anything and it will be considered as string.
- You can use double Quotes (`""`) or single quotes (`''`) to store, both works same. (e.g., `name = "Akarsh"` or `name = 'Akarsh'`)
- **💡 Advanced Tip (Multiline Strings):** আপনি চাইলে তিনটি সিঙ্গেল বা ডাবল কোট (`'''` বা `"""`) ব্যবহার করে মাল্টিলাইন স্ট্রিংও লিখতে পারেন।

## 🚦 Boolean

- **Boolean (`bool`):** There's nothing much to say, this is the data type which will and always give the result of **True** and **False**.
- **⚠️ Crucial Rule:** পাইথনে Boolean-এর `True` এবং `False` লেখার সময় প্রথম অক্ষর অবশ্যই **Capital Letter (বড় হাতের)** হতে হবে। (`true` বা `false` লিখলে কোড এরর দেখাবে)।

পাইথনে উপরের ৩টি বেসিক টাইপ ছাড়াও কিছু বিল্ট-ইন **Collection Data Types** আছে, যেগুলো ছাড়া রিয়েল-লাইফ প্রজেক্ট করা অসম্ভব। এগুলো নোটে অ্যাড করে রাখা খুব জরুরি:

### 1. List (`list`)

- এটি একটি অর্ডার্ড এবং চেঞ্জেবল (Mutable) কালেকশন, যেখানে থার্ড ব্র্যাকেট `[]` এর ভেতরে একাধিক ডেটা কমা দিয়ে রাখা যায়।

Python

```
sports = ["Cricket", "Football", "Tennis"]
```

### 2. Tuple (`tuple`)

- লিস্টের মতোই কিন্তু এটি আনচেঞ্জেবল (Immutable)। একবার তৈরি করলে এর ভেতরের ডেটা পরিবর্তন করা যায় না। এটি ফার্স্ট ব্র্যাকেট `()` দিয়ে লিখতে হয়।

```
coordinates = (23.8103, 90.4125)
```

### 3. Dictionary (`dict`)

- ডেটাকে **Key: Value** পেয়ার হিসেবে ধরে রাখার জন্য এটি ব্যবহার করা হয়। এটি কার্লি ব্রেস `{}` দিয়ে লিখতে হয়।

```
user = {"name": "Akarsh", "age": 12}
```

### 4. Set (`set`)

- ইউনিক বা অনন্য ডেটার আনঅর্ডার্ড কালেকশন। এর ভেতরে কোনো ডুপ্লিকেট ভ্যালু থাকতে পারে না। এটিও `{}` দিয়ে লেখা হয় তবে এতে কোনো Key থাকে না।

```
unique_numbers = {1, 2, 3, 3, 4} # এখানে ডুপ্লিকেট ৩ বাদ পড়ে যাবে
```

> **💡 Useful Tip: `type()` Function**
> 
> 
> পাইথনে কোনো একটি ভেরিয়েবল বা ডেটা আসলে কোন টাইপের, তা জানার জন্য বিল্ট-ইন `type()` ফাংশন ব্যবহার করা হয়।
> 
> ```
> x = 10
> print(type(x))  # Output: <class 'int'>
> ```
>

তোমার নোটে **Data Types** ভালোভাবে কভার করা আছে। এখন যদি এটাকে **Complete Beginner Notes** বানাতে চাও, তাহলে প্রতিটি Data Type-এর সাথে সবচেয়ে বেশি ব্যবহৃত **Methods** এবং **Operations** যোগ করা উচিত।

---

Methods এবং Operations in  Data Types in Python


# 🔢 Numbers

## Integer (`int`)

সব পূর্ণ সংখ্যা (decimal বা fraction ছাড়া) Integer।

```python
age = 22
temperature = -5
```

### Common Operations

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Power
```

### Useful Functions

```python
abs(-20)       # 20
pow(2, 5)      # 32
max(2, 8, 5)   # 8
min(2, 8, 5)   # 2
round(4.7)     # 5
```

---

## Float (`float`)

সব দশমিক সংখ্যা Float।

```python
price = 199.99
pi = 3.1416
```

### Common Functions

```python
round(pi, 2)

float(10)

int(3.9)
```

---

## Complex (`complex`)

```python
z = 2 + 3j
```

### Properties

```python
print(z.real)
print(z.imag)
```

---

# 🔤 Strings (`str`)

যেকোনো Text String হিসেবে সংরক্ষণ করা হয়।

```python
name = "Akarsh"
```

---

## Common Operations

### Concatenation

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

---

### Repetition

```python
print("Hi " * 3)
```

---

### Indexing

```python
name = "Python"

print(name[0])
print(name[-1])
```

---

### Slicing

```python
name = "Python"

print(name[0:3])
print(name[2:])
print(name[:4])
```

---

## Most Used String Methods

### Uppercase

```python
text.upper()
```

---

### Lowercase

```python
text.lower()
```

---

### Title Case

```python
text.title()
```

---

### Capitalize

```python
text.capitalize()
```

---

### Length

```python
len(text)
```

---

### Replace

```python
text.replace("Python", "Java")
```

---

### Find

```python
text.find("th")
```

---

### Count

```python
text.count("o")
```

---

### Startswith

```python
text.startswith("Py")
```

---

### Endswith

```python
text.endswith("on")
```

---

### Split

```python
sentence = "I Love Python"

sentence.split()
```

Output

```python
['I', 'Love', 'Python']
```

---

### Join

```python
words = ["I", "Love", "Python"]

" ".join(words)
```

---

### Strip

```python
text = "   Hello   "

text.strip()
text.lstrip()
text.rstrip()
```

---

### Check Methods

```python
text.isalpha()

text.isdigit()

text.isalnum()

text.isspace()
```

---

# 🚦 Boolean (`bool`)

```python
is_student = True
is_admin = False
```

---

## Boolean Operators

```python
True and False

True or False

not True
```

---

## Comparison Operators

```python
5 > 2

5 < 2

5 == 5

5 != 4

5 >= 3

5 <= 10
```

---

# 📋 List (`list`)

Ordered এবং Mutable Collection।

```python
fruits = ["Apple", "Banana", "Orange"]
```

---

## Access

```python
fruits[0]

fruits[-1]

fruits[1:3]
```

---

## Common Methods

### append()

```python
fruits.append("Mango")
```

---

### insert()

```python
fruits.insert(1, "Grapes")
```

---

### extend()

```python
fruits.extend(["Lemon", "Cherry"])
```

---

### remove()

```python
fruits.remove("Apple")
```

---

### pop()

```python
fruits.pop()

fruits.pop(1)
```

---

### clear()

```python
fruits.clear()
```

---

### sort()

```python
numbers = [5,2,8,1]

numbers.sort()
```

---

### reverse()

```python
numbers.reverse()
```

---

### count()

```python
numbers.count(5)
```

---

### index()

```python
fruits.index("Banana")
```

---

### copy()

```python
new_list = fruits.copy()
```

---

### len()

```python
len(fruits)
```

---

# 📌 Tuple (`tuple`)

Immutable Collection।

```python
point = (10, 20)
```

---

## Operations

```python
point[0]

len(point)
```

---

## Methods

Tuple-এ মাত্র দুইটি Method আছে।

```python
point.count(10)

point.index(20)
```

---

# 📖 Dictionary (`dict`)

Key : Value Pair আকারে Data সংরক্ষণ করে।

```python
user = {
    "name": "Akarsh",
    "age": 20
}
```

---

## Access

```python
user["name"]

user.get("age")
```

---

## Add / Update

```python
user["city"] = "Dhaka"

user["age"] = 21
```

---

## Remove

```python
user.pop("age")

user.popitem()

del user["name"]

user.clear()
```

---

## Useful Methods

### keys()

```python
user.keys()
```

---

### values()

```python
user.values()
```

---

### items()

```python
user.items()
```

---

### update()

```python
user.update({"country": "Bangladesh"})
```

---

### copy()

```python
new_user = user.copy()
```

---

# 🎯 Set (`set`)

Unique এবং Unordered Collection।

```python
numbers = {1,2,3,4}
```

---

## Add

```python
numbers.add(5)
```

---

## Update

```python
numbers.update([6,7])
```

---

## Remove

```python
numbers.remove(2)

numbers.discard(10)

numbers.pop()

numbers.clear()
```

---

## Set Operations

### Union

```python
A | B

A.union(B)
```

---

### Intersection

```python
A & B

A.intersection(B)
```

---

### Difference

```python
A - B

A.difference(B)
```

---

### Symmetric Difference

```python
A ^ B

A.symmetric_difference(B)
```

---

# 🔄 Type Conversion

একটি Data Type থেকে অন্য Data Type-এ রূপান্তর করা।

```python
int("10")

float("3.14")

str(100)

list((1,2,3))

tuple([1,2,3])

set([1,2,2,3])

dict([("name","Akarsh"),("age",20)])
```

---

# 💡 Useful Tip: `type()` Function

কোনো Variable-এর Data Type জানার জন্য `type()` ব্যবহার করা হয়।

```python
x = 10
print(type(x))
# Output: <class 'int'>
```

---

# 🧠 Most Important Built-in Functions

```python
type(x)      # Data type দেখায়

len(data)    # Length বের করে

id(x)        # Memory Address

input()      # User Input

print()      # Output দেখায়

sorted()     # Sort করে

sum()        # যোগফল

max()        # সবচেয়ে বড় Value

min()        # সবচেয়ে ছোট Value

any()        # কোনো একটি True কিনা

all()        # সবগুলো True কিনা

enumerate()  # Index সহ Loop

zip()        # একাধিক Collection একসাথে Iterate

range()      # Number Sequence তৈরি

list()

tuple()

set()

dict()

str()

int()

float()

bool()
```

