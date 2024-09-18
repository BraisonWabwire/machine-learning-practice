import pandas as pd
import datetime

data=pd.read_csv('DailyDelhiClimateTrain.csv')
data.date=pd.to_datetime(data.date)
# print(data.dtypes)
# print(data.head())
datename=data.date.apply(lambda x:x.day_name())
print(datename)