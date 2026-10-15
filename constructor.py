# 1.Parametrized constrctr
# 2. Non -parametrized constructr/default constructr


# A default consturctr does not take any argumnets other than self

# parametrized c

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# # creating an object
# Student1=Student("alice",20)
# print(Student1.name)
# print(Student1.age) 


# How it works:
# when you write:
# student1=stundent("alice",20)
# python automatically calls:
# student.__init__(student1,"alice",20)

# Here:
# self refers to the obj being created (student1)


# non parametrized

# syntax:
# class ClassName:
    # def __init__(self):
    # Initialization

class Student:
    def __init__(self):
        self.name="alice"
        self.age=50
s1=Student()
print(s1.name)
print(s1.age)