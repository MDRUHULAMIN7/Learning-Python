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