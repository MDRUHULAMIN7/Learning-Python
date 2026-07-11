# student = {
#     'name': 'Ruhul',
#     'age': 21,
#     'gpa': 3.85,
#     'subjects': ['Math', 'CS', 'English'],
#     'is_active': True
# }
# print(student['name']) 

# person2 = dict(name='Ruhul', city='Rajshahi')

# print(person2)

# student = {'name': 'Ruhul', 'age': 21}

# # CREATE — নতুন Key-Value যোগ
# student['dept'] = 'Computer'
# student['dept'] = 'Civil'

# student.pop('dept')

# print(student['dept'])

# print(student.get("dept"))


# print(student)  


student = {'name': 'Ruhul', 'age': 21, 'dept': 'Computer'}

# Method 1: Keys মাত্র (default)
for key in student:
    print(key)   # name, age, dept

# Method 2: .keys()
for key in student.keys():
    print(key)

# Method 3: .values()
for value in student.values():
    print(value)   # Ruhul, 21, Computer

# Method 4: .items() — Key ও Value একসাথে (Best Practice)
for key, value in student.items():
    print(f'{key}: {value}')
