#print("hello world python")


# Comments in python
# Comments are something that are ignored by the python
# interpreter
#  We have to use for writing a comment in python
#  Multiline comments are not available in python but we can
# achieve it by using Doc String

# #

# “”” Multiline ”””
#hello this is single line comment

"""
this is multi line comment 
this is multi line comment but this is not comment this is doc string"""


# myName = "ruhul amin"
# print(myName)

# a = 33
# print(type(a))
# b = 3.14
# print(type(b))
# c = 1 + 2j
# print(type(c))

# d =33/2
# print(type(d))

# st = "oidjfsodfjgo"
# st2 = 'oidjfsodfjgo'
# print(type(st2))

# isTrue = True
# print(type(isTrue))

# a = "e"
# print(ord(a))

# a = 101
# print(chr(a))


# a = "ruhul amin "
# print(a[0])
# print(a[-2])
# print(a[0::1])

# name = "Ruhul Amin"

# age = 22
# print(f"my name is {name} and my age is {age}")

# age = str(input("what is your age?")) 
# print(f"age is {age}")  
# print(type(age))

# a = 7
# b = 20      

# print(a+b)
# print(b//a)
# print(b/a)
# print(type(b*a) )

# print(233**43)
# print(49%8)

# a =20 
# print(a)
# a = 30
# print(a)

# a += 10
# print(a)

# a = 44
# b = 33

# a, b = b, a
# print(a)
  
# a = 44
# b = "44"
# print(a == b)
# print(a > b or a > 40)
# print(a > b and a > 40)

# print(not True)
# print(not False)

# print(23 >= 238)

# print("acb" == "abc")

# print(45 < 34 and 45 < 50 )
# print(45 > 34 or 45 < 50 or 45 > 50)

# print(not 12!=12)
# print(True and bool(3))

# fruits = ['apple', 'banana', 'cherry']

# Method 1: সরাসরি element ধরে (Best Practice)
# for fruit in fruits:
#     print(fruit)

# evens = list(range(0, 2, 1)) 
# print(evens)



# numbers = [1,8, 2, 3,3,3, 4, 5]

# # print(numbers.count(3))  # Output: 1

# # numbers.sort(reverse=True)
# # numbers.sort()
# # numbers.reverse()
# # new = numbers.copy()
# # print(new)

# numbers.clear()
# print(numbers)

# a = [1, 2, 3, 4, 5]

# a.append([7,8])
# a.extend([9,10])
# a.insert(0, 0)
# print(a)

# numbers = [3, 1, 7, 2, 9, 4]

# print(len(numbers))   
# print(max(numbers))    
# print(min(numbers))    
# print(sum(numbers))   
# print(sorted(numbers)) 
# print(list(reversed(numbers))) 
# print(5 in numbers) 
# print(7 in numbers)  

# a = (1, 2, 3, 4, 5)
# print(type(a))
# a[1] = 10
# print(a)

# index = a.index(3)
# print(index)

# count = a.count(3)
# print(count)

# b = (6, 7, 8,print(),"hello")

# print(b)

# sets = {1, 2,7, 3,"dddd", 4,3, 5}
# print(type(sets))
# # print(sets[2])

# c = hash("hello")
# print(c)

# d = hash((1,4,3))
# print(d)
# for i in sets:
#     print(i)
# sets.add(11)
# # sets.remove(3)
# sets.discard(3)
# print(sets)

# a = {1,2,3,4,5}
# b = {4,5,3,6,7,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b)) 

# a = {"name": "Ruhul Amin", "age": 22, "city": "Dhaka", "city": "Dhaka",3: "number",3: "number2"}  

# # print(type(a))
# # print(a["city"])
# # print(a.get("age"))
# a[3] = "number3"
# a["country"] = "Bangladesh"
# a.update({"population": "20 million", "language": "Bangla"})
# a.update({"population": "30 million"})
# a.pop("age")
# del a["name"]
# print(a)

# a = {1: "one", 2: "two", 3: "three",4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

# b= {1: "onerr", 12: "twelve", 13: "thirteen",14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}

# for i in b:
#     a[i] = b[i]

# print(a)    

# for i in a.values():
#     print(i)    
# help(dict)

# a = [1, 2, 3, 4, 5]

# b = a.copy()
# b[1] = "ONE"
# print(a,b)

# print(a.items())
# print(a.keys())

# a = {1:10, 2:20, 3:30, 4:40, 5:50}

# sum = 0
# for i in a.values():
#     sum += i
# print(sum)

# a = [1, 2, 3, 4, 5, 2, 3, 23, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 5, 5, 6, 6, 64, 4, 1, 1, 1, 12, 22, 2, 2, 22, 22]

# d = {}
# for i in a:
#     if i in d:
#         print(d[i])
#         d[i]= d[i]+1
#     else:
#         d[i] = 1


# print(d)

# try:
#     a = int(input("enter a number: "))
#     c = 10 / a
#     print(c)
# except ZeroDivisionError:
#     print("you can't divide by zero")
# except ValueError:
#     print("invalid input, please enter a number")
# finally:
#     print("this will always execute")    
# try:
#     a = int(input("enter a number: "))
#     c = 10 / a
#     print(c)
# except Exception as e:
#     print("here is an error: ", e)
# raise Exception("this is a custom error")

# else:
#     print("this will execute if there is no error")   
# finally:
#     print("this will always execute")    

# print("defrgwertertyh")


#### # File Handaling in Python

