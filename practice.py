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

name="my outer name is braison"
def names():
    global name
    name='my inner name is wabwire'
    print(name)

print(name)
names()