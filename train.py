from datetime import datetime
import os
from pandas import read_csv
from datetime import datetime
import pandas as pd


columns = ['adview','views','likes','dislikes','comment','published']

txs = pd.read_csv('ad_org_train.csv', names=columns)

txs.info() # to get summary statistics
txs.head() # to get a feel for the data

#print txs['date'][1:]
txs = txs[1:]

year = lambda x: datetime.strptime(x, "%Y-%m-%d" ).year
txs['year'] = txs['published'].map(year)

day_of_week = lambda x: datetime.strptime(x, "%Y-%m-%d" ).weekday()
txs['day_of_week'] = txs['published'].map(day_of_week)
month = lambda x: datetime.strptime(x, "%Y-%m-%d" ).month
txs['month'] = txs['published'].map(month)
day = lambda x: datetime.strptime(x, "%Y-%m-%d" ).day
txs['day'] = txs['published'].map(day)
# please read docs on how week numbers are calculate
week_number = lambda x: datetime.strptime(x, "%Y-%m-%d" ).strftime('%V')
txs['week_number'] = txs['published'].map(week_number)

seasons = [0,0,1,1,1,2,2,2,3,3,3,0] #dec - feb is winter, then spring, summer, fall etc
season = lambda x: seasons[(datetime.strptime(x, "%Y-%m-%d" ).month-1)]
txs['season'] = txs['published'].map(season)

quarters = [0,0,0,1,1,1,2,2,2,3,3,3] #quarter
quarter = lambda x: quarters[(datetime.strptime(x, "%Y-%m-%d" ).month-1)]
txs['quarter'] = txs['published'].map(quarter)

part_of_months = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2] #quarter
part_of_month = lambda x: part_of_months[(datetime.strptime(x, "%Y-%m-%d" ).day-1)]
txs['part_of_month'] = txs['published'].map(part_of_month)

txs.drop(columns=['published'])

txs.to_csv('new_train_data.csv', index=False)

