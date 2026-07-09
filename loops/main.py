# counter = 0

# while counter < 5:
#     print(f"iteration : {counter}")

#     counter += 1

# name = "Ruhul"

# for i in range(len(name)):
#     print(name[i])

# for char in name:
#     print(char)

# evens = list(range(1, 5, 1)) 
# print(evens)

# numbers = [1,8, 2, 3,3,3,3, 4, 5]

# print(numbers.count(3))  # Output: 1

# numbers.clear()
# print(numbers)


# a = [1, 2, 3, 4, 5]

# a.append([7,8])
# a.extend([9,10])
# a.insert(1, 100)
# print(a)
# n = 6
# factor_sum = 0

# for i in range(1, (n // 2) + 1):
#     if n % i == 0:
#         factor_sum += i

# if factor_sum == n:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")


# print(8//2)



# একটি সংখ্যা ইনপুট নাও। যদি সংখ্যাটি n হয়, তাহলে "hello world" ঠিক n বার প্রিন্ট করো।

# n = int(input("Enter how many time to print Hello World:- "))

# for i in range(n):
#     print("Hello World")

# একটি সংখ্যা n ইনপুট হিসেবে নাও এবং ১ থেকে n পর্যন্ত সব সংখ্যা প্রিন্ট করো।

# n = int(input("Enter the number:- "))

# for i in range(1,n+1):
#     print(i)

# রিভার্স (উল্টো) for লুপ ব্যবহার করে n থেকে 1 পর্যন্ত সংখ্যা প্রিন্ট করো।

# অর্থাৎ, একটি সংখ্যা n ইনপুট নাও এবং n, n-1, n-2, ... , 1 এই ক্রমে প্রিন্ট করো।


# n = int(input("Enter the number:- "))

# for i in range(n,0,-1):
#     print(i)

# Take a number as input and print its table

# n = int(input("Enter the number:- "))

# for i in range(1,11,1):
#     print(f"{n} x {i} = {n*i}")


# Sum up to n terms
# একটি সংখ্যা n ইনপুট নাও এবং ১ থেকে n পর্যন্ত সব সংখ্যার যোগফল প্রিন্ট করো।

# n = int(input("Enter the number:- "))

# sum = 0

# for i in range(1,n+1,1):
#     sum += i

# print(sum)



# Factorial of a number

# একটি সংখ্যার ফ্যাক্টোরিয়াল (Factorial) বের করো।

# ফ্যাক্টোরিয়াল (n!) বলতে ১ থেকে n পর্যন্ত সব সংখ্যার গুণফল বোঝায়।

n = int(input("Enter the number:- "))

fac = 1

for i in range(1,n+1,1):
    fac *= i

print(fac)