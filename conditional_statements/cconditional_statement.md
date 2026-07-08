# Python Conditional Statements

১. Introduction to Control Flow (কন্ট্রোল ফ্লো মেকানিজম)

- **Core Definition:** ডিফল্টভাবে পাইথন স্ক্রিপ্ট ওপর থেকে নিচে লাইন বাই লাইন (Sequential) এক্সিকিউট হয়। কিন্তু বাস্তব অ্যাপ্লিকেশনে নির্দিষ্ট কন্ডিশন বা শর্তের ওপর ভিত্তি করে কোডের কোনো অংশ এক্সিকিউট করা এবং কোনো অংশ স্কিপ করার প্রক্রিয়াকে **Control Flow** বলা হয়।
- **Decision Making:** কন্ডিশনাল স্টেটমেন্ট মূলত প্রোগ্রামের সিদ্ধান্ত নেওয়ার ক্ষমতা (Decision-making) নিয়ন্ত্রণ করে। স্লাইডের লজিক অনুযায়ী, যদি একটি ইনপুট নম্বর ১০ এর চেয়ে বড় হয় তবে প্রোগ্রাম **Task A** রান করবে, আর ছোট হলে **Task B** রান করবে।

## ২. Types of Conditional Statements (সিনট্যাক্স ও মেকানিজম)

পাইথনে মূলত ৩টি ভ্যারিয়েশনে কন্ডিশনাল স্টেটমেন্ট হ্যান্ডেল করা হয়:

### ক) Simple `if` Statement

- **Behavior:** শুধুমাত্র একটি নির্দিষ্ট শর্ত সত্য (`True`) হলে এর ভেতরের ব্লকটি এক্সিকিউট হয়। শর্ত মিথ্যা হলে পাইথন এই ব্লকটি স্কিপ করে চলে যায়।
- **Syntax:**Python
    
    # 
    
    ```
    if condition:
        # Code to execute if condition is True
    ```
    

### খ) Dual Branch `if-else` Statement

- **Behavior:** এখানে দুটি বিকল্প রাস্তা থাকে। শর্ত সত্য হলে `if` ব্লক এক্সিকিউট হয়, আর শর্ত মিথ্যা (`False`) হলে অবধারিতভাবে `else` ব্লকটি এক্সিকিউট হয়।
- **Syntax:**Python
    
    # 
    
    ```
    if condition:
        # Code if condition is True
    else:
        # Code if condition is False
    ```
    

### গ) Multi-Branch `if-elif-else` Ladder

- **Behavior:** যখন ক্রমান্বয়ে একাধিক শর্ত চেক করার প্রয়োজন হয়, তখন এটি ব্যবহৃত হয়। পাইথন ওপর থেকে এক এক করে শর্ত চেক করতে করতে নিচে নামে। যেখানেই প্রথম `True` কন্ডিশন পায়, সেই ব্লকটি রান করে পুরো ল্যাডার বা মই থেকে বের হয়ে যায়। যদি কোনো শর্তই সত্য না হয়, তবে সবার শেষের `else` ব্লকটি এক্সিকিউট হয়।
- **Syntax:**Python
    
    # 
    
    ```
    if condition1:
        # Code if condition1 is True
    elif condition2:
        # Code if condition2 is True
    else:
        # Code if all conditions are False
    ```
    

## ৩. Practical Application: The if-elif Ladder Example

বাস্তব লাইফ উদাহরণ হিসেবে স্লাইডে তাপমাত্রার (Temperature) ওপর ভিত্তি করে কন্ডিশনাল ল্যাডারের একটি চমৎকার ব্যবহারের কথা বলা হয়েছে:

- **Below 0°C** $\rightarrow$ "Freezing Cold ❄️"
- **0°C to 10°C** $\rightarrow$ "Very Cold 🥶"
- **10°C to 20°C** $\rightarrow$ "Cold 🧦"
- **20°C to 30°C** $\rightarrow$ "Pleasant ☁️"
- **30°C to 40°C** $\rightarrow$ "Hot 🔥"
- **Above 40°C** $\rightarrow$ "Very Hot 🫠"

### 🛠️ Production-Ready Python Code Implemetation:

Python

# 

```
# ইউজার থেকে ইনপুট নিয়ে ফ্লোটে কনভার্ট করা
temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing Cold ❄️")
elif 0 <= temperature <= 10:
    print("Very Cold 🥶")
elif 10 < temperature <= 20:
    print("Cold 🧦")
elif 20 < temperature <= 30:
    print("Pleasant ☁️")
elif 30 < temperature <= 40:
    print("Hot 🔥")
else:
    print("Very Hot 🫠")
```

## 🚨 Architectural Deep Dive & Best Practices (ইঞ্জিনিয়ারিং রুলস)

- **১. Indentation Rule (ইনডেন্টেশন মেকানিজম):** পাইথনে অন্য প্রোগ্রামিং ভাষার মতো কোড ব্লক বোঝানোর জন্য কোনো কার্লি ব্রেস `{}` ব্যবহার করা হয় না। এখানে কোড ব্লকের সীমানা নির্ধারণ করা হয় **Indentation (ডিফল্টভাবে ৪টি স্পেস)** দিয়ে। ইনডেন্টেশনে সামান্য ভুল হলে পাইথন কম্পাইল টাইমে **`IndentationError`** থ্রো করে।
- **২. Logical Operators Integration:** স্লাইডে উল্লেখ আছে যে কন্ডিশনাল ব্লকের ভেতরে আমরা `and`, `or`, `not` লজিক্যাল অপারেটর ব্যবহার করে জটিল কন্ডিশন তৈরি করতে পারি। যেমন: ভোটার আইডি চেকিংয়ের জন্য:Python
    
    # 
    
    ```
    age = int(input("Enter age: "))
    has_nid = True
    
    if age >= 18 and has_nid:
        print("Valid voter")
    ```
    
- **৩. Code Optimization Note (Order of Conditions):** মাল্টিপল `elif`  লেখার সময় সবসময় যে কন্ডিশনটি আগে সত্য হওয়ার সম্ভাবনা বেশি, সেটিকে উপরে রাখা উচিত। এতে পাইথনকে অপ্রয়োজনীয় নিচের কন্ডিশনগুলো চেক করতে হয় না, যা সিপিইউ সাইকেল বা এক্সিকিউশন টাইম বাঁচায়।