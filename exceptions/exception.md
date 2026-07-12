# Python Exceptions — Error Handling

## ১. Exception কী?

- **Definition:** Exception হলো program চলার সময় ঘটা অপ্রত্যাশিত ঘটনা যা program ঊর স্বাভাবিক flow ভাঙ্গে দেয়।
- **Error vs Exception:** তিন ধরনের সমস্যা আছে:
    - **SyntaxError** — code লেখার সময় স্বয়ংক্রিয়ভাবে ধরা পড়ে, run হয়ই না
    - **Exception** — run হওয়ার সময় ঘটে — এগুলো handle করা যায়
    - **LogicalError** — code সঠিক কিন্তু output ভুল, handle করা যায় না

```
print('Start')
print(10 / 0)   # ❌ ZeroDivisionError — program এখানেই থেমে যায়
print('End')    # ❌ এ লাইন কখনো run হবে না!
```

## ২. Common Built-in Exceptions

| Exception | কারণ | উদাহরণ |
| --- | --- | --- |
| `ZeroDivisionError` | 0 দিয়ে ভাগ | `10 / 0` |
| `NameError` | নাম হয়নি এমন variable | `print(x)` |
| `TypeError` | ধরন মিলছে না | `'5' + 5` |
| `ValueError` | সঠিক ধরন কিন্তু ভুল মান | `int('hello')` |
| `IndexError` | Index সীমার বাইরে | `lst[99]` |
| `KeyError` | Dictionary key নেই | `d['x']` |
| `AttributeError` | Attribute নেই | `'str'.push()` |
| `FileNotFoundError` | File পাওয়া যাচ্ছে না | `open('x.txt')` |
| `ImportError` | Module নেই | `import xyz` |
| `StopIteration` | Iterator শেষ | `next()` অতিরিক্ত |

## ৩. Exception Handling — try / except / else / finally / raise

### ৩.১ Keywords ঎র ভূমিকা

| Keyword | কাজ |
| --- | --- |
| `try` | যে code ঎ exception ঘটতে পারে তা wrap করো |
| `except` | Exception ঘটলে এখানে handle করো |
| `else` | Exception না ঘটলে এই block চলবে |
| `finally` | Exception হোক বা না, সবসময় চলবে |
| `raise` | নিজে থেকে exception throw করা |

### ৩.২ সম্পূর্ণ উদাহরণ

```
try:
    num = int(input('সংখ্যা দাও: '))
    result = 100 / num
except ValueError:
    print('স্বাভাবিক সংখ্যা দাও!')
except ZeroDivisionError:
    print('শূন্য দিয়ে ভাগ হয় না!')
else:
    print(f'ফলাফল: {result}')  # exception না হলে চলবে
finally:
    print('সবসময় চলে')  # exception হোক বা না
```

## ৪. Multiple Except Blocks

```
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('শূন্য দিয়ে ভাগ হয় না')
        return None
    except TypeError:
        print('সর্বপ্রথম সংখ্যা দিতে হবে')
        return None

# Multiple exception একসাথে catch:
try:
    x = int('hello')
except (ValueError, TypeError) as e:
    print(f'ভুল হয়েছে: {e}')

# সবাইকে catch করা (bare except — avoid করা ভালো)
try:
    risky_code()
except Exception as e:   # সব built-in exception ধরে
    print(f'Error: {e}')
```

## ৫. raise — নিজে Exception Throw করা

```
def set_age(age):
    if age < 0:
        raise ValueError(f'বয়স negative হতে পারে না: {age}')
    if age > 150:
        raise ValueError(f'বয়স অবাস্তব: {age}')
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # বয়স negative হতে পারে না: -5
```

## ৬. Custom Exceptions — নিজের Exception তৈরি

```
# Custom exception class
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'ব্যালেন্স কম: আছে {balance}, দরকার {amount}')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    result = withdraw(500, 1000)
except InsufficientBalanceError as e:
    print(e)   # ব্যালেন্স কম: আছে 500, দরকার 1000
```

## ৭. Exception Chaining — Advanced

```
try:
    d = {'a': 1}
    val = d['b']   # KeyError
except KeyError as e:
    raise ValueError('সঠিক key দাও') from e   # মূল error সহ নতুন raise
```

## ৮. Real-world Patterns

### File পড়া

```
try:
    with open('data.txt', 'r') as f:   # 'with' ব্যবহার করো — auto close
        content = f.read()
except FileNotFoundError:
    print('File পাওয়া যাচ্ছে না')
except PermissionError:
    print('পড়ার অনুমতি নেই')
```

### User Input Validate

```
def get_positive_number():
    while True:
        try:
            n = int(input('ধনাত্মক সংখ্যা দাও: '))
            if n <= 0:
                raise ValueError('ধনাত্মক হতে হবে')
            return n
        except ValueError as e:
            print(f'ভুল: {e}, আবার চেষ্টা করো')
```

### API Call / Network Request ঊ

```
import json

def safe_parse(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f'Invalid JSON: {e}')
        return None
```

## ৯. Best Practices — Professional অভ্যাস

- **Bare `except:` avoid করো** — `except Exception as e:` ব্যবহার করো
- **Specific exception catch করো** — `except ZeroDivisionError` না শুধু `except Exception`
- **`finally` তে cleanup** — database connection close, file close
- **`with` statement** — file/resource handle করার সর্বোত্তম উপায়
- **Custom Exception** — নিজের app ঊর জন্য meaningful error names তৈরি করো
- **Exception message সর্বদা log করো** — debug সহজ হয়

```
# ❌ বাজে প্রথা:
try:
    risky()
except:
    pass   # নির্বিকারে সব গ্রাস করে!

# ✅ সঠিক প্রথা:
try:
    risky()
except SpecificError as e:
    logger.error(f'Error: {e}')   # log করো
    raise   # বা বাবুদের জানাও
```

## ১০. Exception Hierarchy (Simplified)

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── IndexError
    ├── KeyError
    ├── ZeroDivisionError
    ├── FileNotFoundError
    ├── AttributeError
    └── ... আরও অনেক
```

## 🚀 Expert Roadmap

1. **`logging` module** — `print` ঊর বদলে proper logging — production code ঊ অপরিহার্য
2. **Context Manager** — `__enter__`, `__exit__` implement করা
3. **`traceback` module** — detailed error info
4. **Assertions** — `assert` দিয়ে testing করা
5. **Exception in OOP** — custom exception hierarchy তৈরি