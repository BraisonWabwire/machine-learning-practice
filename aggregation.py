import pandas as pd
data=pd.read_csv('employees.csv')
# print(data.head())
# print(data.info())
# print(data.SALARY.sum())
print(data. JOB_ID.value_counts())
print(data. JOB_ID.mode())
