# numbers = [10, 20, 30]
# numbers[1] = 99          # index 1 এর মান বদলানো হলো
# print(numbers)


# mixed = [42, 'Ruhul', 3.14, True, [1, 2]]   # এক List এ সব ধরনের data!
# print(mixed)

# evens = list(range(0, 11, 4))  # [0, 2, 4, 6, 8, 10]

# print(evens)

# letters = list('Ruhul')         # ['R', 'u', 'h', 'u', 'l']

# print(letters)

fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']

# print(fruits[0])
# # Slicing: list[start:stop:step]
# print(fruits[1:4:2])

# for fruit in fruits:
#     print(fruit)

# Method 2: Index ধরে
# for i in range(len(fruits)):
#     print(f'Index {i}: {fruits[i]}')
 

 # Method 3: enumerate() — index ও element একসাথে (Expert style)
# for index, fruit in enumerate(fruits):
#     print(f'{index} -> {fruit}')

# While loop দিয়ে
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1


# matrix = [
#     [1,2],
#     [4,5],
#     [6,7,8]
# ]


# print(matrix[2][2])

numbers = [3, -1, 7, -5, 2, -8, 9, 0]

positives = [x for x in numbers if x > 0]

print(positives)