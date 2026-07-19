# def decorate(func):
#     def wrapper():
#         print(' i will print myself before the function hello')
#         func()
#         print(' i will print after the function')
#     return wrapper

# @decorate
# def hello():
#     print("hello i am ruhul amin ")

# hello()

# def my_decorator(func):

#     def wrapper(a,b):
#         print("Before")
#         func(a,b)
#         print("After")

#     return wrapper


# @my_decorator
# def add(a, b):
#     print(a + b)


# add(3, 5)

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#         print(sum)
#     print(sum)

# addition(2,4,6,7)

def addition(**kwargs):
    for i in kwargs.values():
        print(i)
    print(kwargs)

addition(a =  12,b = 14 , d = 11)