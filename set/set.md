# Python Set — Data Structure

## ১. Set কী এবং কেন ব্যবহার করি?

- **Definition:** Set হলো একটি Unordered, Mutable collection যাতে কোনো duplicate element থাকতে পারে না। `{ }` curly braces দিয়ে তৈরি হয়।
- **Real-life Analogy:** একটি unique ID card সংগ্রহের মতো — কোনো মান দুইবার থাকতে পারে না।
- **Set কোথায় ব্যবহার হয়?**
    - Duplicate element বাদ দিতে
    - Membership check — `in` operator O(1) সময়ে কাজ করে (List ঎র চেয়ে দ্রুত)
    - Mathematical set operations — union, intersection, difference

## ২. Set ঎র ৪ বৈশিষ্ট্য (Powers)

### ২.১ Mutable — পরিবর্তন যোগ্য (add/remove সম্ভব)

```
s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}
```

### ২.২ No Duplicates — Unique elements মাত্র

```
s = {1, 2, 2, 3, 3, 3}
print(s)   # {1, 2, 3} — duplicate আপনা থেকেই বাদ যায়!

# List থেকে duplicate বাদ দেওয়ার সবচেয়ে দ্রুত উপায়:
my_list = [1, 2, 2, 3, 3, 4]
unique = list(set(my_list))
print(unique)   # [1, 2, 3, 4]
```

### ২.৩ Unordered — Index দিয়ে access হয় না

```
s = {10, 20, 30}
print(s[0])   # ❌ TypeError: 'set' object is not subscriptable
```

### ২.৪ Semi-Heterogeneous — সব ধরনের data নয়

```
# ✅ Hashable types (immutable): int, str, tuple, float
s = {1, 'hello', (1, 2), 3.14}

# ❌ Unhashable types (mutable): list, dict, set
s = {[1, 2]}   # TypeError: unhashable type: 'list'
```

## ৩. Hashing — Set কীভাবে কাজ করে (Internal Mechanism)

- প্রতিটি value দিয়ে `hash()` function চালাদেওয়া হয় — সেটা memory address হিসেবে কাজ করে
- Hash নিয়ে সেই element memory ঎ সংরক্ষণ হয়, তাই order নেই
- Mutable object হাশ নন-ডিটার্মিনিস্টিক, তাই Set ঎ রাখা যায় না

```
print(hash(42))        # কোনো সংখ্যা
print(hash('hello'))   # কোনো সংখ্যা
print(hash([1, 2]))    # ❌ TypeError: unhashable type: 'list'
```

## ৪. Set তৈরি করা

```
# খালি Set — {} দিয়ে খালি Set তৈরি হয় না! খালি {} হলো dict
empty_set = set()   # ✅ সঠিক

# সরাসরি
numbers = {1, 2, 3, 4, 5}

# List থেকে
my_set = set([1, 2, 2, 3, 3])   # {1, 2, 3}

# String থেকে
letters = set('hello')   # {'h', 'e', 'l', 'o'} — duplicate 'l' বাদ
```

> **⚠️ গুরুত্বপূর্ণ:** `empty = {}` হলো empty **dict**, empty **set** নয়। Set তৈরি করতে `set()` লিখতে হবে।
> 

## ৫. Set Traversing

Index নেই, শুধু for loop দিয়ে traverse করা যায় — কিন্তু ক্রম guarantee নেই।

```
s = {10, 20, 30, 40}

for element in s:
    print(element)   # ক্রম যেকোনো হতে পারে!

# Membership check — O(1) সময়ে (List O(n) সময় নেয়!)
print(20 in s)   # True
print(99 in s)   # False
```

## ৬. Set Methods — সর্বমোট

```
s = {1, 2, 3}

# যোগ করা
s.add(4)        # {1, 2, 3, 4} — একটি element
s.update([5, 6, 6])  # {1, 2, 3, 4, 5, 6} — বাদে বাদে iterable বা add

# মুছে দেওয়া
s.remove(2)     # element না থাকলে KeyError!
s.discard(99)   # element না থাকলেও error নেই
popped = s.pop()  # যেকোনো একটি random element মুছে ফেরায়
s.clear()       # সব element মুছে দেয়, empty set
```

| Method | কাজ | Error যদি না থাকে? |
| --- | --- | --- |
| `add(x)` | একটি element যোগ | না, duplicate ignore |
| `update(iterable)` | বাদে বাদে যোগ | না |
| `remove(x)` | element মুছে | হ্যাঁ, KeyError |
| `discard(x)` | element মুছে | না, নিরাপদ |
| `pop()` | Random element মুছে ও ফেরায় | হ্যাঁ, empty হলে |
| `clear()` | সব মুছে | না |
| `copy()` | Shallow copy | না |

## ৭. Set Operations — Mathematical Operations

```
A = {1, 2, 3}
B = {3, 4, 5}

# Union — দুটো Set ঎র সব element
union_set = A.union(B)                  # {1, 2, 3, 4, 5}
union_set = A | B                       # shortcut

# Intersection — দুটো Set ঎ যা সমান আছে
intersection = A.intersection(B)        # {3}
intersection = A & B                    # shortcut

# Difference — A ঎ আছে কিন্তু B ঎ নেই
difference = A.difference(B)            # {1, 2}
difference = A - B                      # shortcut

# Symmetric Difference — দুটোতে যা বাদে বাদে আছে (সাধারণতা নয়)
symmetric = A.symmetric_difference(B)  # {1, 2, 4, 5}
symmetric = A ^ B                       # shortcut
```

| Operation | Method | Shortcut | ফলাফল |
| --- | --- | --- | --- |
| Union | `.union(B)` | `A \ | B` |
| Intersection | `.intersection(B)` | `A & B` | শুধু common |
| Difference | `.difference(B)` | `A - B` | A ঎ আছে, B ঎ নেই |
| Symmetric Diff | `.symmetric_difference(B)` | `A ^ B` | শুধু যা ভিন্ন |

## ৮. আরও কিছু গুরুত্বপূর্ণ Methods

```
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {4, 5}

# issubset — A কি B ঎র ভেতরে আছে?
print(A.issubset(B))      # True
print(A <= B)             # shortcut — True

# issuperset — A কি B ঊর superset?
print(B.issuperset(A))    # True
print(B >= A)             # True

# isdisjoint — কোনো common element নেই?
print(A.isdisjoint(C))    # True — কোনো মিল নেই
print(A.isdisjoint(B))    # False — মিল আছে
```

## ৯. Frozenset — Immutable Set

```
# Frozenset পরিবর্তন না, তাই Dict key হতে পারে
fs = frozenset([1, 2, 3])
print(fs)   # frozenset({1, 2, 3})

d = {fs: 'একটি Set কে key হিসেবে ব্যবহার'}
print(d[fs])   # এটি Set কে key হিসেবে ব্যবহার
```

## ১০. Common Interview Questions

### List থেকে Duplicate বাদ দেওয়া

```
data = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(data))
print(sorted(unique))   # [1, 2, 3, 4, 5]
```

### দুটি List ঎র Common Elements

```
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = list(set(a) & set(b))
print(common)   # [3, 4]
```

### দুটি List Merge — Duplicate নেই

```
a = [1, 2, 3]
b = [3, 4, 5]
merged_unique = list(set(a) | set(b))
print(sorted(merged_unique))   # [1, 2, 3, 4, 5]
```

## ১১. Best Practices

- **`remove()` ঎র বদলে `discard()` ব্যবহার করো** — element না থাকলে error নেই
- **Membership check** ঊ Set অনেক দ্রুত — O(1) vs List তে O(n)
- **Duplicate remove করতে** `set()` সবচেয়ে সহজ
- **Order দরकার হলে** Set ব্যবহার করো না — List ব্যবহার করো

## 🚀 Expert Roadmap

1. **Dictionary** — Key-Value pair, real-world ঎ সবচেয়ে বেশি ব্যবহৃত
2. **`collections.Counter`** — element frequency গণনার জন্য Set ঊর মতো
3. **Time Complexity:** `add()`, `in`, `remove()` — সর্বাই O(1) average case