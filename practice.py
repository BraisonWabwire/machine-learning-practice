# subjects={
#     'maths':20,
#     'english':50,
#     'kiswahili':80,
#     'geography':90,
#     'biology':61,
#     'CRE':80,
#     'business':75
# }


# for key,value in subjects.items():
#     if value>40:
#         print("you have passed:",key>40)


# for character in "Braison wabwire":
#     for x in range(3):
#         print(character,x)


# for character in "analytics":
#     if (character=='a') or (character=='i'):
#         print("x",end=' ')
#     else:
#         print(character,end='x')
    
# number=10
# while number>5:
#     print(number,end=' ')
#     number=number-1
#     if number==8:
#         number=3

# number=0
# for number in range(10):
#     if number==4:
#         continue
#     print(number,end=" ")

# number = 10
# while number > 3:
#     if number % 2 == 0:
#         number = number - 1  # Move the decrement here to avoid infinite loop
#         continue
#     number = number - 1
#     print(number, end="")
# else:
#     print(number, end=" ")
#     number = number - 1

# list=[1,2,3,4,4,6,2,5]
# names=['braison','wabwire','daniel']
# for x,y in zip(list,names):
#     print(x,y,end=" ")

# list=[1,2,3,4,4,6,2,5]
# print(list[1])

# list=[
#     ["A","B","C"],
#     ["B","A","C"],
#     ["C","B","A"]
#     ]
# print(list[0][0])

students_marks=[
    ['name',['A','B','C','D','E']],
    ['Braison',['80','83','77','90','85']],
    ['James',['70','63','97','50','45']],
    ['Lydia',['67','63','76','40','95']],
    ['Harvid',['57','56','33','78','76']]
]
# print(students_marks[0][1][1])
# student_with_marks_in_B=[]
# for student in students_marks [1:]:
#     name=student[0]
#     marks_subject_B=student[1][1]
#     # print(name,marks_subject_B,end=" ")

#     student_with_marks_in_B.append([marks_subject_B,name])
#     print(sorted(student_with_marks_in_B,reverse=True))

# student_with_marks_in_C=[]
# for student in students_marks[1:]:
#     name=student[0]
#     marks_in_C=student[1][2]
#     student_with_marks_in_C.append([marks_in_C,name])
#     print(sorted(student_with_marks_in_C))

# my_list=['lakshay','sanad','aravind','aishwarya','prateek']
# my_list=['haryana','punjab','rajasthan','karnataka','goa']
# find_a=[]
# for name in my_list:
#     letter_a=name.find('a')
#     find_a.append(letter_a)
#     print(find_a)

# for s in my_list:
#     split_a=s.split('a')
#     find_a.append(len(split_a))
#     print(find_a)

# def welcome():
#     print("Welcome again to python coding")

# welcome()


# def home(name):
#     return "welcome to maseno " + name

# name = input("Enter your name: ")  # No need to use str() as input() already returns a string
# print(home(name))  # This will print the output returned by the function

# def areaRectangle(length,width):
#     area=length*width
#     return print('The area of the rectangle is: ',area)
# length=int(input("Enter the length:"))
# width=int(input("Enter the width:"))

# areaRectangle(length,width)

# def function(*args):
#     for r in args:
#         print(r)
# function(1,2,'braison',1,'james')

# def function(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# function(a=3,b=4,t=11)

# name="variable outside function"
# def names():
#     global name
#     name='variable inside function'
#     return print(name)

# names()
# print(name)

# x=lambda a: a +20
# print(x(20))



# def odd(x):
#     if x%2==0:
#         return True
#     else:
#         return False
    
# numbers=[10,15,34,20,12,9,45,12]

# filtered_numbers=list(filter(lambda x: x %2!=0,numbers))
# print(filtered_numbers)

# def factorial(n):
#     if (n==0) or (n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# value_n=int(input("Enter value of n:"))
# result=factorial(value_n)
# print(result)

# def isDivisibleThree(x):
#     return x%3==0

# def isDivisibleTwo(x):
#     return x%2==0

# x=list(filter(isDivisibleThree, range(0,31)))
# print(x)
# y=list(filter(isDivisibleTwo,range(1,10)))
# print(y)
# z=list(filter(lambda x: x%2==0,range(2,30)))
# print(z)

# def square(x):
#     return x*x

# x=list(map(square,[1,2,3,4,5]))
# print(x)

from functools import reduce

def add(x,y):
    return x+y
def mult(x,y):
    return x*y

# a=reduce(add,[1,2,3,4,5,6,7])
# print(a)

# r=reduce(add,["my"," ","name"," ","is"," ","braison"])
# print(r)

# def red(n):
#     return reduce(mult,range(1, n+1))

# print(red(4))

# def number(n):
#     if n==2:
#         return 1
#     else:
#         return number(n-1)+(n+1)
    
# print(number(5))

# m=open('C:/Users/brais/OneDrive/Desktop/machine learning practice/m.txt')
# m.seek(15)
# print(m.read())

import datetime
datetime_obj=datetime.datetime.now()
today_obj=datetime.date.today()
print(datetime_obj)
print(today_obj)
