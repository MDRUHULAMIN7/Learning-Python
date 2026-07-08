# Python Input and Output

## ১. Output Internals: The print() Function

- **The Core Mechanism:** পাইথনে টার্মিনালে কোনো আউটপুট বা রেজাল্ট দেখানোর জন্য `print()` হলো একমাত্র স্ট্যান্ডার্ড বিল্ট-ইন ফাংশন। তবে ব্যাকএন্ডে এটি মূলত সিস্টেমের `sys.stdout` স্ট্রিমের মাধ্যমে ডেটা রাইট (write) করে।
- **Dynamic String Formatting (f-strings):** স্লাইডের উদাহরণ অনুযায়ী, স্ট্রিংয়ের ভেতরে ভেরিয়েবলের মান ডাইনামিকালি বসানোর সবচেয়ে আধুনিক এবং ফাস্ট উপায় হলো **f-string (Formatted String Literal)**।
    - **Syntax:** স্ট্রিংয়ের কোটেশনের ঠিক আগে একটি `f` বা `F` বসাতে হয় এবং ভেরিয়েবলগুলোকে কার্লি ব্রেস `{}` এর ভেতরে রাখতে হয়।
    - *Example:*Python
        
        ```
        name = input("Enter your name: ")  #
        print(f"Hello, {name}! Welcome to Python programming.")  #
        ```
        
- **💡 Engineer Note (Performance):** পুরানো পাইথন সংস্করণের `%` ফরম্যাটিং বা `.format()` মেথডের তুলনায় `f-string` অনেক বেশি দ্রুত কাজ করে, কারণ এটি রানটাইমে সরাসরি অপ্টিমাইজড বাইটকোড হিসেবে ইভালুয়েট হয়।

## ২. Input Internals: The input() Function

- **The Core Mechanism:** ইউজারের কাছ থেকে কনসোল বা টার্মিনালের মাধ্যমে ডেটা গ্রহণ করার জন্য `input()` ফাংশন ব্যবহার করা হয়। যখনই পাইথন এই ফাংশনটি পায়, সে প্রোগ্রাম এক্সিকিউশন পজ (pause) করে ইউজারের কিবোর্ড ইনপুটের জন্য অপেক্ষা করে।
- **The String-Only Rule (⚠️ অত্যন্ত গুরুত্বপূর্ণ):** ইউজার কিবোর্ড থেকে সংখ্যা (`12`), দশমিক (`3.14`) কিংবা টেক্সট যা-ই ইনপুট দিক না কেন, পাইথনের `input()` ফাংশন সেটিকে অবধারিতভাবে **String (`str`)** ডাটা টাইপ হিসেবেই মেমরিতে স্টোর করে। কারণ, স্ট্রিং যেকোনো ক্যারেক্টারকে নিজের ভেতর ধারণ করতে পারে।

## ৩. Data Type Casting for Input Statements (টাইপ কাস্টিং)

যেহেতু ইনপুট ডিফল্টভাবে স্ট্রিং হিসেবে আসে, তাই গাণিতিক বা লজিক্যাল অপারেশনের জন্য ডেভেলপারকে ম্যানুয়ালি সেই স্ট্রিং ডেটাকে অন্য টাইপে রূপান্তর (Type Cast) করতে হয়।

### ক) Accepting Numbers / Integers (পূর্ণসংখ্যা গ্রহণ)

ইউজারের কাছ থেকে বয়স, রোল বা যেকোনো পূর্ণসংখ্যা ইনপুট নিয়ে সরাসরি গাণিতিক কাজ করতে চাইলে `input()` ফাংশনটিকে `int()` ফাংশন দিয়ে র‍্যাপ (Wrap) করতে হয়।

Python

```
# স্লাইডের প্রশ্ন অনুযায়ী: ইউজার থেকে বয়স নেওয়া এবং প্রিন্ট করা
age = int(input("Enter your age: "))  #
print(f"Next year you will be {age + 1} years old.")
```

### খ) Accepting Floating-Point Numbers (দশমিক সংখ্যা গ্রহণ)

যদি ইনপুট হিসেবে কোনো দশমিক ভ্যালু (যেমন: প্রাইস, সিজিপিএ, তাপমাত্রা) আসার সম্ভাবনা থাকে, তবে আমাদের `float()` ফাংশন ব্যবহার করতে হবে।

Python

```
# ইউজার থেকে যেকোনো সংখ্যা বা দশমিক সংখ্যা নেওয়া
price = float(input("Enter the product price: "))
```

## Edge Cases & Architectural Exceptions (ইঞ্জিনিয়ারিং সতর্কতা)

একজন সফটওয়্যার ইঞ্জিনিয়ার হিসেবে এই `input()` এবং টাইপ কাস্টিং ব্যবহারের সময় নিচের হ্যান্ডলিংগুলো মাথায় রাখা বাধ্যতামূলক:

- **The `ValueError` Exception:** আপনি যখন `int(input())` ব্যবহার করছেন, ইউজার যদি কিবোর্ড থেকে সংখ্যার বদলে কোনো টেক্সট (যেমন: `"twenty"`) ইনপুট দেয়, তবে পাইথন সাথে সাথে **`ValueError: invalid literal for int()`** এরর দিয়ে পুরো অ্যাপ্লিকেশন ক্র্যাশ করাবে। প্রোডাকশন লেভেলে এটি হ্যান্ডেল করার জন্য `try-except` ব্লক ব্যবহার করা হয়:Python
    
    ```
    try:
        user_number = int(input("Enter a valid number: "))
    except ValueError:
        print("Error: You must enter digits only!")
    ```
    
- **Security Risk:** পাইথন ৩-এ `input()` নিরাপদ হলেও পুরানো পাইথন ২-এ `input()` ফাংশনটি ইউজারের ইনপুটকে সরাসরি পাইথন কোড হিসেবে এক্সিকিউট করে ফেলত (যা ছিল একটি বড় Security Vulnerability)। পাইথন ৩-এ এটি সম্পূর্ণ ফিক্সড এবং নিরাপদ।



# ১. `print()` Function এর সব গুরুত্বপূর্ণ Parameters

অনেকেই শুধু `print()` ব্যবহার করে, কিন্তু এর কিছু powerful parameter আছে।

## `sep` (Separator)

একাধিক ভ্যালুর মাঝে কী থাকবে তা নির্ধারণ করে।

```python
print("Python", "Java", "C++")
```

Output

```
Python Java C++
```

Default separator হলো space (`" "`)

---

Custom Separator

```python
print("Python", "Java", "C++", sep="-")
```

Output

```
Python-Java-C++
```

---

আরও উদাহরণ

```python
print(10, 20, 30, sep=" | ")
```

Output

```
10 | 20 | 30
```

---

# ২. `end` Parameter

Default হিসেবে print শেষে newline (`\n`) দেয়।

```python
print("Hello")
print("World")
```

Output

```
Hello
World
```

---

এখন

```python
print("Hello", end=" ")
print("World")
```

Output

```
Hello World
```

---

আরও উদাহরণ

```python
for i in range(5):
    print(i, end=", ")
```

Output

```
0, 1, 2, 3, 4,
```

---

# ৩. Escape Characters

Special Character লিখতে ব্যবহার হয়।

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New Line     |
| `\t`   | Tab          |
| `\\`   | Backslash    |
| `\"`   | Double Quote |
| `\'`   | Single Quote |

Example

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

```python
print("Name\tAge")
```

Output

```
Name    Age
```

---

# ৪. Multiple Input একসাথে নেওয়া

```python
a, b = input("Enter two numbers: ").split()
```

যদি ইউজার লেখে

```
10 20
```

তাহলে

```
a = "10"
b = "20"
```

---

Integer বানাতে

```python
a, b = map(int, input().split())
```

Input

```
10 20
```

Output

```
a = 10
b = 20
```

---

Float

```python
x, y = map(float, input().split())
```

---

# ৫. List Input নেওয়া

```python
numbers = list(map(int, input().split()))
```

Input

```
10 20 30 40
```

Output

```
[10, 20, 30, 40]
```

এটা Competitive Programming-এ সবচেয়ে বেশি ব্যবহার হয়।

---

# ৬. Type Checking

ইনপুটের টাইপ যাচাই করা।

```python
age = int(input())

print(type(age))
```

Output

```
<class 'int'>
```

---

# ৭. String Methods Input এর সাথে

```python
name = input().strip()
```

`strip()` সামনে ও পিছনের space মুছে দেয়।

---

```python
name = input().lower()
```

সব ছোট হাতের অক্ষর।

---

```python
name = input().upper()
```

সব বড় হাতের অক্ষর।

---

```python
name = input().title()
```

প্রতিটি শব্দের প্রথম অক্ষর বড়।

---

# ৮. Boolean Input

Python-এ

```python
flag = bool(input())
```

এভাবে নেওয়া উচিত নয়।

কারণ

```python
bool("False")
```

Output

```
True
```

কারণ খালি string ছাড়া সব string True।

সঠিক উপায়

```python
choice = input().lower()

if choice == "true":
    flag = True
else:
    flag = False
```

---

# ৯. Input Validation

```python
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Invalid Input")
```

Production Code-এ এটি খুবই গুরুত্বপূর্ণ।

---

# ১০. EOF Input

বড় বড় Input File পড়ার সময়।

```python
import sys

for line in sys.stdin:
    print(line)
```

Competitive Programming-এ ব্যবহৃত হয়।

---

# ১১. Faster Input

বড় Data হলে

```python
import sys

data = sys.stdin.readline()
```

এটি

```python
input()
```

থেকে দ্রুত।

---

# ১২. Faster Output

```python
import sys

sys.stdout.write("Hello")
```

এটিও `print()` অপেক্ষা কিছু ক্ষেত্রে দ্রুত।

---

# ১৩. Raw String

```python
print(r"C:\Users\Amin")
```

Output

```
C:\Users\Amin
```

---

# ১৪. Formatting Numbers

```python
price = 1234.56789

print(f"{price:.2f}")
```

Output

```
1234.57
```

---

Comma Formatting

```python
salary = 1000000

print(f"{salary:,}")
```

Output

```
1,000,000
```

---

# ১৫. Print Different Bases

```python
num = 20

print(bin(num))
print(oct(num))
print(hex(num))
```

Output

```
0b10100
0o24
0x14
```

---

# ১৬. Input Buffering

যখন

```python
input()
```

ব্যবহার হয়,

Python

* Execution Pause করে
* Keyboard Buffer থেকে Input নেয়
* Enter Press হওয়া পর্যন্ত অপেক্ষা করে
* তারপর String Return করে

---

# ১৭. Command Line Input (Advanced)

শুধু Terminal থেকে

```python
import sys

print(sys.argv)
```

Run

```bash
python main.py Ruhul 20
```

Output

```
['main.py', 'Ruhul', '20']
```

---

# ১৮. File Input / Output (I/O)

Input সবসময় Keyboard থেকেই আসে না।

```python
with open("data.txt") as file:
    text = file.read()

print(text)
```

Output File-এও লেখা যায়।

```python
with open("result.txt", "w") as file:
    file.write("Hello")
```

---

# ১৯. Common Mistakes

❌

```python
age = input()
print(age + 1)
```

Error

```
TypeError
```

✔

```python
age = int(input())
print(age + 1)
```

---

❌

```python
num = int(input())

# User enters
12.5
```

Error

```
ValueError
```

✔

```python
num = float(input())
```

---

# ২০. Interview Questions

* `input()` সবসময় কোন data type return করে?
* `print()`-এর `sep` এবং `end` কী?
* `input()` এবং `sys.stdin.readline()`-এর পার্থক্য কী?
* `print()` এবং `sys.stdout.write()`-এর পার্থক্য কী?
* `map()` কীভাবে input processing সহজ করে?
* `split()` কী কাজ করে?
* `strip()` কেন ব্যবহার করা হয়?
* `f-string` কেন `.format()`-এর চেয়ে বেশি জনপ্রিয়?
* `try-except` কেন input handling-এ গুরুত্বপূর্ণ?
* `type casting` কী এবং কেন দরকার?

---

## শেখার অগ্রাধিকার (Beginner → Advanced)

১. `print()`
২. `input()`
৩. `int()`, `float()`, `str()`
৪. `sep`, `end`
৫. Escape Characters
৬. `split()`
৭. `map()`
৮. List Input
৯. `type()`
১০. String Methods (`strip()`, `lower()`, `upper()`)
১১. `try-except`
১২. `sys.stdin.readline()`
১৩. `sys.stdout.write()`
১৪. File I/O
১৫. Command Line Arguments (`sys.argv`)


