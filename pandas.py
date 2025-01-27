# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12j2DlvnY61-kVIlP5Ui1ziaq96U1N3IK

**HOW TO ADD LIST AS PANDAS DATA FRAME**
"""

#IMPORT LIBRARY
# empty data frame
import pandas as pd
df=pd.DataFrame()
df

#Data frame from list
city=['Dhaka','Delhi','Tokyo','Katmundu']
df=pd.DataFrame(city)
city

# It is not execute as pandas dataframe so what's the problem
city=['Dhaka','Delhi','Tokyo','Katmundu']
df=pd.DataFrame(city)
df
#Now the list is ready for pandas data frame

row,col= df.shape
df.shape

# set column name while making data frame
df=pd.DataFrame(city, columns=['City Name'])
df

#set column name  while making data frame
df=pd.DataFrame(city,columns=['City Asia'], index=['City-1','City-2','City-3','City-4'])
df

#add 2 column
city=['Dhaka','Delhi','Tokyo','Katmundu']
city2=['Wasington','New Jersey','London','-']
df2=pd.DataFrame(zip(city,city2), columns=['City in Asia','City in America'], index=['City-1','City-2','City-3','City-4'])
df2

df2.shape

# To save time, instead of initiating 2 variables, you can input "2D List" as one variable ....
#city3[[],[].........]--- " one 3rd bracket denote one ROW "
city3=[['Dhaka','Wasington'],['Delhi','New Jersey'],['Tokyo','London'],['Katmundu','-']]
df3=pd.DataFrame(city3, columns=['City in Asia','City in America'], index=['City-1','City-2','City-3','City-4'])
df3

"""**Dictionary as data **"""

city1=['Dhaka','Delhi','Tokyo','Katmundu']
city2=['Wasington','New Jersey','London','-']
dict1={
    'City in Asia':city1,
    'City in America':city2
}
df4=pd.DataFrame(dict1, index=['City-1','City-2','City-3','City-4'])
df4

"""**HOW TO READ EXCEL DATA FILE**

>First upload the data sheet from your pc to colab. Than copy the path and read the pasted path.....


"""

df5=pd.read_csv('/content/Screentime-App-Details-Dataset.csv')
df5