## ১. File কী এবং File Handling কী?

- **File:** একটি File হলো ডিস্কে সংরক্ষিত থাকা data যার একটি নাম এবং extension থাকে — যেমন `.py`, `.txt`, `.mp3`, `.csv` ইত্যাদি।
- **File Handling:** File ের উপর CRUD (Create, Read, Update, Delete) operation পরিচালনা করাকে File Handling বলে।
- **কেন দরকার?**
    - Program বন্ধ হওয়ার পরেও data সংরক্ষণ করে রাখা (Persistent storage)
    - Log file, configuration file, dataset পড়া
    - Report, CSV, JSON file তৈরি করা

## ২. open() Function — File Handling র সূত্রপাত

```
# Syntax
file = open('filename', mode)
```

Python এ file নিয়ে কাজ করতে হলে প্রথমে `open()` function দিয়ে file টি open করতে হয়।

## ৩. File Modes — বিস্তারিত

| Mode | নাম | কাজ | File না থাকলে? |
| --- | --- | --- | --- |
| `'r'` | Read (default) | পড়া, file অবশ্যই থাকতে হবে | `FileNotFoundError` |
| `'w'` | Write | লেখা, না থাকলে তৈরি করে, থাকলে সব মুছে নতুন করে লেখা হয় | নতুন তৈরি হয় |
| `'a'` | Append | শেষে নতুন content যোগ করে, পুরানো data থাকে | নতুন তৈরি হয় |
| `'x'` | Create (exclusive) | নতুন file তৈরি করে | আগে থাকলে `FileExistsError` |
| `'r+'` | Read + Write | পড়া ও লেখা দুটোই | `FileNotFoundError` |
| `'rb'` / `'wb'` | Binary mode | Image, video, pdf ঎র মতো binary file ঎র জন্য | mode অনুযায়ী |

```
# বিভিন্ন mode এ open করার উদাহরণ
f1 = open('data.txt', 'r')    # Read mode
f2 = open('data.txt', 'w')    # Write mode — সাবধান! পুরানো data মুছে যাবে
f3 = open('data.txt', 'a')    # Append mode
f4 = open('new.txt', 'x')     # Create mode — আগে থাকলে error
```

## ৪. File Read করা — ৩টি পদ্ধতি

```
file = open('myfile.txt', 'r')

# Method 1: read() — সম্পূর্ন file একসাথে string হিসেবে পড়ে
print(file.read())

file.seek(0)   # আবার শুরু থেকে পড়তে cursor reset করতে হবে

# Method 2: readline() — ১টি line পড়ে
print(file.readline())   # প্রথম line
print(file.readline())   # দ্বিতীয় line

file.seek(0)

# Method 3: readlines() — সব line একটি List হিসেবে পড়ে
lines = file.readlines()
print(lines)   # ['line1\n', 'line2\n', 'line3\n']

file.close()
```

| Method | কাজ | Return Type |
| --- | --- | --- |
| `read()` | পুরো file একসাথে পড়ে | string |
| `read(n)` | প্রথম n character পড়ে | string |
| `readline()` | এক line পড়ে | string |
| `readlines()` | সব line list হিসেবে পড়ে | list |

## ৫. File Write করা

```
# write() — একটি string লেখে
file = open('myfile.txt', 'w')   # ⚠️ পুরানো content মুছে যাবে!
file.write('স্বাগতম Python File Handling এ!\n')
file.write('এই হলো দ্বিতীয় line\n')
file.close()

# writelines() — একইসাথে অনেক line লেখা
file = open('myfile.txt', 'w')
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
file.writelines(lines)
file.close()

# append mode — পুরানো data থেকে দ্বিতীয় নামানো
file = open('myfile.txt', 'a')
file.write('এই লাইনতা শেষে যোগ হলো\n')
file.close()
```

> **⚠️ গুরুত্বপূর্ণ সতর্কতা:** `'w'` mode ঎ file open করলে পুরানো সব content **মুছে যায়**! data harano রোধ করতে হ। চাই॑লে `'a'` (append) mode ব্যবহার করো।
> 

## ৬. close() — File বন্ধ করা কেন দরকার

File open করার পর এটি মান্যুযালি close করা উচিত — না হলে:

- Memory leak হতে পারে
- Data ভুলভাবে file ঎ লেখা হতে পারে (buffer flush না হওয়ার কারণে)
- File lock সমস্যা হতে পারে

```
file = open('myfile.txt', 'r')
print(file.read())
file.close()   # মান্যুযালি close

# একটি সমস্যা: exception ঘটলে close() নাও চলতে পারে!
file = open('myfile.txt', 'r')
data = file.read()
result = 10 / 0   # এখানে error এসে থেমে যাবে
file.close()      # ❌ এই line কখনো তালাবে না! File open থেকেই যাবে
```

## ৭. with Statement — সবচেয়ে সঠিক পদ্ধতি (Best Practice)

`with` keyword ব্যবহার করলে file স্বয়ংক্রিয়ভাবে close হয়ে যায় — exception ঘটলেও কোনো সমস্যা হয় না।

```
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)
# এখানে স্বয়ংক্রিয়ভাবে f.close() হয়ে যায়, নিজে লিখতে হয় না!

# Exception ঘটলেও file ঠিকমতো close হবে
with open('data.txt', 'r') as f:
    content = f.read()
    result = 10 / 0   # error এসে ও close হয়েই যাবে!

# Write ঎ with statement
with open('output.txt', 'w') as f:
    f.write('Auto-closed file!\n')

# মাল্টিপল file একসাথে (Python 3.10+)
with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    fout.write(fin.read())
```

> **🧠 Expert Advice:** Professional code এ সবসময় `with` statement ব্যবহার করো — এটা Python ঎র স্থাপিত best practice (PEP 8 এর অন্তর্গত)। মানুয়াল `close()` ভুলে যাওয়ার সম্ভাবনা থাকে না।
> 

## ৮. File এ Traverse করা (Line by Line)

```
# Method 1: readlines() + loop
with open('data.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())   # strip() দিয়ে \n মুছে দেওয়া হলো

# Method 2: সরাসরি file object দিয়ে loop (Memory efficient — Expert Style)
with open('data.txt', 'r') as f:
    for line in f:   # পুরো file মেমরিতে নেয় না, এক line করে পড়ে
        print(line.strip())
```

> **💡 Expert Insight:** বড় File ঎র েক্ষেত্রে Method 2 ব্যবহার করো — `readlines()` পুরো file memory এ নেয়, কিন্তু `for line in f` একটি line এ নেয় — মেমরি efficient!
> 

## ৯. File Pointer / Cursor — seek() ও tell()

```
with open('data.txt', 'r') as f:
    print(f.tell())     # 0 — cursor position
    content = f.read(10)
    print(f.tell())     # 10 — cursor 10 character এসেছে

    f.seek(0)           # cursor আবার শুরুতে নিয়ে যাওয়া
    print(f.read(5))    # প্রথম 5 character আবার পড়ুক
```

## ১০. File Existence Check — os module

```
import os

# File আছে কিনা দেখো
if os.path.exists('data.txt'):
    print('File আছে')
else:
    print('File নেই')

# নিরাপদে read করা
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        print(f.read())
else:
    print('File পাওয়া যায়নি!')

# File মুছে দেওয়া
if os.path.exists('old.txt'):
    os.remove('old.txt')
```

## ১১. Exception Handling ঎র সাথে File Handling (Real Pattern)

```
try:
    with open('config.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print('config.txt পাওয়া যায়নি!')
except PermissionError:
    print('Permission নেই!')
else:
    print('সফলভাবে পড়া হয়েছে')
finally:
    print('Operation শেষ')
```

## ১২. Practical Examples — বাস্তব এবং Interview Pattern

### Word Count করা

```
with open('data.txt', 'r') as f:
    content = f.read()
    word_count = len(content.split())
    print(f'মোট শব্দ: {word_count}')
```

### Line Count করা

```
with open('data.txt', 'r') as f:
    lines = f.readlines()
    print(f'মোট line: {len(lines)}')
```

### File Copy করা

```
with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
    dest.write(src.read())
```

### CSV ঎র মতো Data লেখা

```
students = [
    'Ruhul,21,3.85',
    'Foysal,20,3.70',
    'Toha,22,3.90'
]

with open('students.csv', 'w') as f:
    f.write('name,age,gpa\n')
    for student in students:
        f.write(student + '\n')
```

### Log File এ Append করা (Real-world Pattern)

```
import datetime

def log_message(message):
    with open('app.log', 'a') as f:
        timestamp = datetime.datetime.now()
        f.write(f'[{timestamp}] {message}\n')

log_message('Application started')
log_message('User logged in')
```

## ১৩. JSON File Handling — Expert Level

```
import json

# Dictionary একে JSON file ঎ লেখা
data = {'name': 'Ruhul', 'age': 21, 'skills': ['Python', 'JS']}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)   # indent দিয়ে pretty print

# JSON file থেকে পড়া
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data['name'])   # Ruhul
```

## ১৪. Best Practices — Professional অভ্যাস

- **`with` statement সবসময় ব্যবহার করো** — manual `close()` ভুল হতে পারে
- **`'w'` mode সতর্কতার সাথে ব্যবহার করো** — পুরানো data মুছে যায়!
- **Exception handling যোগ করো** — `FileNotFoundError` সবসময় হতে পারে
- **বড় file ঎ লাইন দিয়ে পড়ো** — `for line in f`, `readlines()` না
- **JSON/CSV ঎র জন্য নির্দিষ্ট module ব্যবহার করো** — `json`, `csv` module শব্দ manipulation ঎র চেয়ে দ্রুত ও সঠিক

## 🚀 Expert Roadmap

1. **`csv` module** — CSV file read/write এর জন্য নির্দিষ্ট module
2. **`pathlib` module** — Modern, Object-oriented file path handling
3. **Binary File Handling** — `'rb'`, `'wb'` mode দিয়ে image, video, pdf
4. **`pickle` module** — Python object সরাসরি file এ সংরক্ষণ (serialization)
5. **`shutil` module** — File copy, move, delete এর advanced operation