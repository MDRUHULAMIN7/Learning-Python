# def greet(name):
#     print(f'hellow world,{name}')

# greet("Ruhul")  # এখানে call করলে তবেই চলবে

# def introduce(name, city, age,message="wellcome"):
#     print(f'আমি {name}, {city} থেকে, বয়স {age}{message}')

# introduce('ruhul', 'rajshahi', 21)  # ক্রম গুরুত্বপূর্ণ!


# def register(name, roll, department):
#     print(f'{department} বিভাগে {name}, রোল: {roll}')

# # Keyword argument — ক্রম মিলছে না, তবুও সঠিক কাজ করবে
# register(roll='2301', department='Computer', name='Ruhul')



# def sum_all(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# print(sum_all(2,3,4,5,6))

# def user_info(**details):
#     for key,value in details.items():
#         print(f'{key} : {value}')

# user_info(name='Ruhul', roll='2301', dept='Computer', gpa=3.8)

#lamda function
# sum = lambda a,b: a + b

# print(sum(2,3))