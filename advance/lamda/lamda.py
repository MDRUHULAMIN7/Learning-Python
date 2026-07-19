# square = lambda x: x ** 2   # একই কাজ
# print(square(4))   # Output: 16

# # Multiple arguments
# add = lambda x, y: x + y
# print(add(3, 5))   # 8

# # If-Else expression
# check_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
# print(check_even(7))   # Output: Odd

# a= [1,2,3,4,5]

# # result = map(lambda x: x*2,a)

# def double(x):
#     return x*2

# result = map(double,a)

# print(list(result))


# a= [1,2,3,4,5]

# def even(x):
#     if x%2 == 0:
#         return True
    
#     else:
#         return False
    
# result = filter(even , a)

# print(list(result))

nums = [-3, -1, 0, 2, 5, -2, 8]
positives = list(filter(lambda x: x > 0, nums))
print(positives) 