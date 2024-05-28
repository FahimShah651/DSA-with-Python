
import os
def tclear():
    # os.system('cls' if os.name == 'nt' else 'clear')
    os.system("cls")
 
#######################################################################
#import numpy as np
tclear()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class intro:
    
#     def __init__(self,name ,age) :
#         self.name = name
#         self.age = age
#     def prin(self):
#         print(self.name)
#         print(self.age)
#     def __str__(self) -> str:
#         return f"name : {self.name} , age : {self.age}"
        
    
# class ch_intro(intro):
#     def __init__(self, name, age,sch):
#         super().__init__(name, age)
#         self.school = sch
#     def ch_prin(self):
#         print(f"name :{self.name} , age : {self.age} , school : {self.school} ")
#     # def prin(self):                                 # overide function
#     #     print("child print function is called ")
    
# int1 = intro("hell",23)
# int1.prin()
# child = ch_intro("haris",23,"al abbas")
# child.prin()
# child.ch_prin()
# child.prin()


# class my_iter:
#     def __iteer__(self):
#        self.x = 1
#        return self
#     def __next__(self):
#         x = self.x
#         self.x +=1
#         return x
#     def __str__(self) -> str:
#         print("object called")
        
# obj = my_iter()
# num = obj.__iteer__()
# for i in range(10):
#    print(next(num))

import turtle as t
tu = t.Screen()
fs = t.Turtle()
fs.begin_fill("red")
for i in range(0,10):
       fs.circle(10*i)
       
    