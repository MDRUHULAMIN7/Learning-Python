# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age

#     def __str__(self):
#         return f"how are you {self.name}"
    
#     def __add__(self, other):
#         return f"sum of  ages { self.age + other.age}"
    
# obj = Animal('lion',33)
# obj2 = Animal('tiger',44)


# print(obj,obj2)
# print(obj+obj2)

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __str__(self):
        return f"{self.name} ({self.gpa})"


s1 = Student("Ruhul", 3.85)
s2 = Student("Foysal", 3.70)
s3 = Student("Toha", 3.85)

print(s1 == s3)
# True

print(s1 > s2)
# True

print(s2 < s1)
# True
