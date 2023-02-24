import pandas as pd
import numpy as np
# class and Inheritence

class Person:
    def __init__(self, firtName, LastName):
        self.__fName = firtName
        self.Lname = LastName
    def prinName(self) -> str:
        print(self.__fName, self.Lname)

class Teacher(Person):
    def __init__(self, firtName, LastName, name):
        super().__init__(firtName, LastName)
        self.fName=firtName
        self.lName=LastName
        self.name = name
    def printNameL(self):
        print(self.name)
    def totalFee(self, a, b) -> int:
        return a+b

t = Teacher("Md", "Owais", "ozair")
# print(t.__fName,t.Lname)
t.prinName()
t.printNameL()
x=t.totalFee(4,5)
print(x)
p=Person("md", "owais")
p.prinName()
# print(p.__fName)
# class Student:
#     pass



# list comprehension

# list1 = [5,4,6,7,8,2]
# # list_com = {list1[i]:f"items{i}" for i in range(len(list1))}
# # print(list_com)
# list2 = [elem * elem for elem in list1]
# print(list2)

# dict1 = {i*i: f"items{i}" for i in range(8)}
# print(dict1)

# dict2 = {val:key for key,val in dict1.items()}
# print(dict2)

# tup1 = (1,2,4,5,6,8)
# tup2 = tuple(elem*elem for elem in tup1)
# print(tup2)
# list1 = list()
# list1.append(2)
# list1.append(4)
# list1.append((2,3,4))
# list1.extend([1,2,3,4])
# list1.insert(0,0)
# del(list1[0])
# print(list1)
# del(list1[2])
# list1[0]=10
# print(list1)


# list2 = list(map(lambda x: x*x, list1))
# list3 = list(filter(lambda x: x > 4, list1))
# list4 = reduce(lambda x,y: x+y, list1)
# print(list2)
# print(list3)

