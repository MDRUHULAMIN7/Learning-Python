# class Factory:
#     a = 12 #attribute 
#     def hello(self): #method
#         print("how are you")

#     print("I am getting Initialized ")

# # print(Factory().a)

# Factory().hello()

# ruhul = Factory()

# print(ruhul.a)


class Student:
    college = "RPI"
   
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll 

s1 = Student('Ruhul',21)
s2 = Student('Toha',33)

        
print(s1.name)
print(s2.name)
print(s2.college)


# s1.college = 'BUBT'
Student.college = 'Uttara'

print(s2.college)
print(s1.college)

