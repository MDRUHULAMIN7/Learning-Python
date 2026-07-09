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
n = 6
factor_sum = 0

for i in range(1, (n // 2) + 1):
    if n % i == 0:
        factor_sum += i

if factor_sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


print(8//2)