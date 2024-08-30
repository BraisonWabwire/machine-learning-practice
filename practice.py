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
for student in students_marks [1:]:
    name=student[0]
    marks_subject_B=student[1][1]
    print(name,marks_subject_B)