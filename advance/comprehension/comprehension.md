# Comprehensions (List, Dict, Set)

## ১. Comprehension কী?

Loop ও condition এক লাইনে লিখে List/Dict/Set তৈরি করার Pythonic পদ্ধতি। সাধারণ loop এর চেয়ে দ্রুত ও পরিষ্কার।

## ২. List Comprehension

```
# Syntax: [expression for item in iterable if condition]

# সাধারণ loop:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List Comprehension:
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# Condition সহ:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]

# If-Else সহ (ternary):
labels = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]
print(labels)    # ['Even', 'Odd', 'Even', 'Odd', 'Even']

# Nested:
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)    # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## ৩. Dictionary Comprehension

```
# Syntax: {key: value for item in iterable if condition}

# Even সংখ্যার square dict:
evens = {x: x*x for x in range(10) if x % 2 == 0}
print(evens)   # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Key-Value swap:
d = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in d.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}

# Word frequency:
words = ['apple', 'banana', 'apple', 'cherry']
freq = {w: words.count(w) for w in set(words)}
print(freq)   # {'cherry': 1, 'banana': 1, 'apple': 2}
```

## ৪. Set Comprehension

```
# Syntax: {expression for item in iterable if condition}

# Even square (unique):
unique_even_squares = {x*x for x in range(10) if x % 2 == 0}
print(unique_even_squares)   # {0, 4, 16, 36, 64}

# Duplicate বাদ দিয়ে:
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(unique)   # {1, 2, 3, 4}
```

## ৫. কখন Comprehension ব্যবহার করবে?

| পরিস্থিতি                 | করণীয় |
| ----------------------  | --- |
| Simple transform/filter | Comprehension ব্যবহার করো |
| জটিল বহু-step logic | Regular loop — পড়তে সহজ |
| Nested comprehension বেশি গভীর | Loop ব্যবহার করো |

> **💡 Rule of Thumb:** Comprehension এক লাইনে fit করলে ব্যবহার করো — না হলে loop বেশি readable।
>