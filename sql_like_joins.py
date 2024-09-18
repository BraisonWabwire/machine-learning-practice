import pandas as pd
students_data=pd.DataFrame({
    'roll_number':[101,102,103,104,105],
    'names':['Braison','calvin','james','elijah','mathew'],
    'grades':['A','B','A','c','B'],
    'marks':[28,22,27,14,18],
    'city':['nakuru','nairobi','nakuru','mombasa','kericho']
})
# print(students_data)

state_mapping=pd.DataFrame({
    'city':['nakuru','nairobi','mombasa'],
    'state':['nakuru','nairobi','mombasa']
})
# print(state_mapping)
students_data_merged=students_data.merge(state_mapping,how='left', on='city')
print(students_data_merged)

