# Encapsulation

## ১. Encapsulation কী?

* **Encapsulation** হলো Data (Variables) এবং Code (Methods/Functions)-কে একটি **Class**-এর ভেতরে একত্রে রাখা।
* এটি Class-এর অভ্যন্তরীণ তথ্য (Internal Details) লুকিয়ে রাখে এবং শুধুমাত্র প্রয়োজনীয় অংশ ব্যবহার করার সুযোগ দেয়।
* **Real-life Analogy:** একটি ATM Machine-এর ভেতরে কীভাবে কাজ হয়, তা আমরা জানি না। আমরা শুধু Screen ও Button ব্যবহার করি। ভেতরের জটিলতা আমাদের থেকে লুকানো থাকে।

### সুবিধা

* **Data Protection** — Data অনাকাঙ্ক্ষিত পরিবর্তন থেকে সুরক্ষিত থাকে।
* **Code Organization** — Code আরও পরিষ্কার ও সহজে ব্যবস্থাপনা করা যায়।
* **Access Control** — কোন Data বা Method বাইরে থেকে Access করা যাবে, তা নিয়ন্ত্রণ করা যায়।

---

# ২. Access Modifiers — ৩ ধরনের

## ২.১ Public

কোনো Prefix ব্যবহার করা হয় না। Python-এ Default হিসেবে সব Attribute ও Method **Public** হয়।

* Class-এর ভেতর থেকে Access করা যায়।
* Object-এর মাধ্যমে বাইরে থেকেও Access করা যায়।
* Subclass থেকেও Access করা যায়।

```python
class Student:
    def __init__(self):
        self.name = "Ruhul"   # Public

s = Student()
print(s.name)

# Output:
# Ruhul
```

---

## ২.২ Protected

Protected Member-এর আগে একটি Underscore (`_`) ব্যবহার করা হয়।

> **⚠️ মনে রাখবে:** এটি শুধুমাত্র একটি **Convention**। Python এটি কঠোরভাবে বাধ্যতামূলক করে না। বাইরে থেকেও Access করা যায়, তবে সরাসরি Access না করাই ভালো।

```python
class Student:
    def __init__(self):
        self._age = 21

s = Student()

print(s._age)

# Output:
# 21
```

Protected Member সাধারণত Parent ও Child Class-এর মধ্যে ব্যবহারের জন্য রাখা হয়।

---

## ২.৩ Private

Private Member-এর আগে দুটি Underscore (`__`) ব্যবহার করা হয়।

Python এটি **Name Mangling** ব্যবহার করে সংরক্ষণ করে, ফলে Class-এর বাইরে থেকে সরাসরি Access করা যায় না।

```python
class Student:
    def __init__(self):
        self.__salary = 50000

s = Student()

# print(s.__salary)
# ❌ AttributeError
```

Python আসলে এটিকে নিচের নামে সংরক্ষণ করে—

```python
print(s._Student__salary)

# Output:
# 50000
```

> **⚠️ এটি শুধুমাত্র শেখার জন্য দেখানো হয়েছে। বাস্তবে এভাবে Private Attribute Access করা উচিত নয়।**

---

## সম্পূর্ণ উদাহরণ

```python
class Demo:
    def __init__(self):
        self.name = "Public Member"       # Public
        self._age = 21                    # Protected
        self.__salary = 50000             # Private

    def show(self):
        print("Inside the Class:")
        print("Public:", self.name)
        print("Protected:", self._age)
        print("Private:", self.__salary)


d = Demo()

d.show()

# Output:
# Inside the Class:
# Public: Public Member
# Protected: 21
# Private: 50000

print(d.name)
# Public Member

print(d._age)
# 21

# print(d.__salary)
# ❌ AttributeError

print(d._Demo__salary)
# 50000
```

---

## Access Modifier Summary

| Type      | Syntax        | বাইরে থেকে Access                              | ব্যবহার                    |
| --------- | ------------- | ---------------------------------------------- | -------------------------- |
| Public    | `self.name`   | ✅ হ্যাঁ                                        | সাধারণ Data                |
| Protected | `self._name`  | ⚠️ সম্ভব, তবে Convention অনুযায়ী করা উচিত নয় | Parent ও Child Class       |
| Private   | `self.__name` | ❌ না                                           | সংবেদনশীল (Sensitive) Data |

---

# ৩. Getter ও Setter — Private Data Access করার সঠিক উপায়

Private Attribute বাইরে থেকে নিরাপদভাবে পড়া (Read) বা পরিবর্তন (Modify) করার জন্য Getter এবং Setter Method ব্যবহার করা হয়।

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance Negative হতে পারে না!")

        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount


acc = BankAccount("Ruhul", 5000)

print(acc.get_balance())
# 5000

acc.deposit(2000)

print(acc.get_balance())
# 7000

acc.set_balance(10000)

print(acc.get_balance())
# 10000

# acc.set_balance(-500)
# ❌ ValueError
```

---

# ৪. `@property` — Pythonic Getter & Setter

Python-এ Getter ও Setter লেখার সবচেয়ে সুন্দর ও Recommended উপায় হলো `@property` ব্যবহার করা।

```python
class Student:
    def __init__(self, name, gpa):
        self._name = name
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if value < 0 or value > 4.0:
            raise ValueError("GPA অবশ্যই 0 থেকে 4-এর মধ্যে হতে হবে!")

        self.__gpa = value


s = Student("Ruhul", 3.85)

print(s.gpa)
# 3.85

s.gpa = 3.90

print(s.gpa)
# 3.90

# s.gpa = 5.0
# ❌ ValueError
```

> **💡 সুবিধা:** `get_gpa()` বা `set_gpa()` Method আলাদাভাবে Call করতে হয় না। সাধারণ Variable-এর মতো ব্যবহার করা যায়।

---

# ৫. বাস্তব উদাহরণ — User Profile

```python
class UserProfile:
    def __init__(self, username, email, password):
        self.username = username      # Public
        self._email = email           # Protected
        self.__password = password    # Private

    def login(self, password):
        if password == self.__password:
            print(f"{self.username} সফলভাবে Login করেছে!")
        else:
            print("ভুল Password!")

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password সফলভাবে পরিবর্তন করা হয়েছে!")
        else:
            print("পুরোনো Password সঠিক নয়!")


user = UserProfile(
    "ruhul_amin",
    "ruhul@mail.com",
    "secret123"
)

print(user.username)
# ruhul_amin

print(user._email)
# ruhul@mail.com

# print(user.__password)
# ❌ AttributeError

user.login("secret123")
# ruhul_amin সফলভাবে Login করেছে!

user.login("wrong")
# ভুল Password!

user.change_password("secret123", "new_pass")
# Password সফলভাবে পরিবর্তন করা হয়েছে!
```

---

# ৬. Quick Reference

```python
class Example:

    pub = "Public"
    _pro = "Protected"
    __pri = "Private"
```

| Member  | Access Level            |
| ------- | ----------------------- |
| `pub`   | Public                  |
| `_pro`  | Protected (Convention)  |
| `__pri` | Private (Name Mangling) |

---

# সারসংক্ষেপ

| Topic         | কী শেখা হলো                                                                       |
| ------------- | --------------------------------------------------------------------------------- |
| Encapsulation | Data ও Method-কে একটি Class-এর ভেতরে একত্রে রাখা এবং Data সুরক্ষিত রাখা।          |
| Public        | যেকোনো জায়গা থেকে Access করা যায়।                                               |
| Protected     | Convention অনুযায়ী Parent ও Child Class-এর জন্য ব্যবহৃত হয়।                     |
| Private       | শুধুমাত্র Class-এর ভেতরে ব্যবহার করার জন্য।                                       |
| Getter        | Private Data নিরাপদভাবে পড়ার Method।                                             |
| Setter        | Private Data নিয়ন্ত্রিতভাবে পরিবর্তনের Method।                                   |
| `@property`   | Pythonic Getter ও Setter তৈরির সবচেয়ে ভালো উপায়।                                |
| Name Mangling | Private Attribute-কে `_ClassName__attribute` আকারে সংরক্ষণ করার Python-এর পদ্ধতি। |

---

## 🚀 পরবর্তী Topic

**Abstraction** — জটিল Implementation লুকিয়ে রেখে শুধুমাত্র প্রয়োজনীয় Interface ব্যবহারকারীর সামনে উপস্থাপন করা। এটি Object-Oriented Programming (OOP)-এর চতুর্থ মূল Pillar।
