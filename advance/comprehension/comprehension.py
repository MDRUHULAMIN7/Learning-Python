# a = 227
# print('even') if a%2== 0 else print('odd')

# l = [i for i in range(1,21) if i%2 == 0 ]
# print(l)

evens = {x: x*x for x in range(10) if x % 2 == 0}
print(evens) 

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(unique)   # {1, 2, 3, 4}