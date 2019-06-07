import pandas as pd # used to manupulate data and tables
from  matplotlib import pyplot as plt #used to plot data or tables
import itertools #to sort data before plotting

import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange
import random

#simple plotting example
# x = [1, 2, 3]
# y = [1, 4, 9]
# z = [20, 4, 0]

# plt.plot(x,y)
# plt.plot(x, z)
# plt.title('test plot')
# plt.xlabel('x')
# plt.ylabel('y and z')
# plt.legend(['this is y', 'this is z'])
# plt.show()

#using panda
data = pd.read_csv('food_price.csv') #loading csv file 
# pd.set_option('display.max_columns', 2000) #display full column
# print(data.head()) # view the first 5 data of the csv file or see the data structure
# print(type(data)) # to see what type the data is (dataframe for table like data)
# print(data.Region) #to grab a single column
# print(type(data.Region)) # to see what type of data it is(SERIES type is to store series of data)
# print(data.Region[1]) #to grab a single data from a specific column
# print(data.cmname) #list a specific column
# print(data.cmname.unique()) #list all the unique data for a column
# print(data[data['cmname']== 'Fuel (petrol-gasoline) - Retail']) #get all data from a unique item
# petro = data[data['cmname']== 'Fuel (petrol-gasoline) - Retail'] #save to a variable
# plt.plot(petro.date, list(map(float,petro.price))) # plot the data but not ordered bad plot and petro.price has to be converted to float
#plot for a unique data
# plt.xticks(rotation=90) # large title will be tilted 30 degree
# ax = plt.gca() # get current figure
# for label in ax.get_xaxis().get_ticklabels()[::2]: # every 2 labels are invisible
#     label.set_visible(False)
# plt.title('petro')
# plt.xlabel('date')
# plt.ylabel('price')
# plt.tight_layout()
# plt.show()


# f = data[data['cmname']== 'Fuel (kerosene) - Retail']
# a = f[f['admname']=='Oromia']
# print(data.admname.unique())
# print(data.cmname.unique())
# print(a)

kerosene = data[data['cmname']== 'Fuel (kerosene) - Retail']
petrol = data[data['cmname'] == 'Fuel (petrol-gasoline) - Retail']
diesel = data[data['cmname']== 'Fuel (diesel) - Retail']

# print(diesel)
# print(petrol)
# print(kerosene)

plt.plot(kerosene.date, list(map(float,kerosene.price)), 'r--')
plt.plot(kerosene.date, list(map(float,petrol.price)))
plt.plot(kerosene.date, list(map(float,diesel.price)))
plt.xticks(rotation=90) # large title will be tilted 30 degree
ax = plt.gca() # get current figure
for label in ax.get_xaxis().get_ticklabels()[::2]: # every 2 labels are invisible
    label.set_visible(False)
plt.xlabel('date')
plt.ylabel('price')
plt.legend(['kerosene', 'petrol', 'diesel'])
plt.tight_layout()
plt.show()