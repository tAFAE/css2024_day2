# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:50:32 2024

@author: ptmab
"""

import pandas as pd
file = pd.read_csv("C:/Users/ptmab/css2024_day2/data_02/iris.csv")

"""
Absolute Path:
    C:/Users/ptmab/css2024_day2/data_02/iris.csv
Relative Path:
   iris.csv
"""
file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
url = "https://raw.githubusercontent.com/tAFAE/css2024_day1/main/country_data.csv"
file =pd.read_csv(url)
column_names =['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
file = pd.read_csv(url, header=None, names = column_names)
file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")
file = pd.read_excel("data_02/residentdoctors.xlsx")
file = pd.read_json("data_02/student_data.json")
print(file)
#df = dataframe#
#df = pd.read_csv(url)
#print(df.info())
#print(df.describe())
#df =pd.resd_csv("https://codingsummers-9os2173.slack.com/files/U06F46T7GBW/F06GAGZP39S/accelerometer_data.csv", names = ["date_time", "x","y", "z"])
df = pd.read_csv("data_02/country_data_index.csv", index_col=0)
df = pd.read_excel("data_02/residentdoctors.xlsx")
print(df.info())
#to add a column to the excel sheet, you use the following code
#CHECK PYTHON REGULAR EXPRESSIONS
df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
#df["UPPER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
print(df.info())
#the column is added as a string hence we should convert it to an integer
#df["LOWER_AGE"] = df["AGEDIST"].astype(int)
#df["UPPER_AGE"] = df["AGEDIST"].astype(int)
print(df.info())

"""
Working with dates
10-01-2024 -UK
01-10-2024
"""
df =pd.read_csv("data_02/time_series_data.csv", index_col=0)
print(df.info())
#uSUALLY THE DATES ARE PICKED AS STRINGS SO TO CONVERT THEM TO DATE FORMAT 
#df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())
df["Year"] = df["Date"].dt.year
#There are some built in functions on pandas to modify the code
#For example .str, .extract, .astype"
df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)
df.drop(index=26, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())
avg_cal = df["Calories"].mean ()
df["Calories"].fillna(avg_cal, inplace= True)

"""
Best practices
"""
#To remove all the nan in the data you can use the following code
df.dropna(inplace = True)
df = df.reset_index(drop=True)
#df.loc[7,'Duration'] = 45
df['Duration'] = df['Duration'] .replace([450], 50)
print(df)
#pd.set_option("display.max_rows", None)
###################################

df = pd.read_csv("data_02/iris.csv")
col_names = df.columns.tolist()
print(col_names)
df["sepal_length_sq"] = df["sepal_length"].apply(lambda x:x**2)
grouped = df.groupby("class")
mean_square_values = grouped["sepal_length_sq"].mean()
print(mean_square_values)

###################################

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split1.csv")
#To add these two files together one can 
df = pd.concat([df1, df2], ignore_index=True)

###################################
#To add files with different names of columns one must use this code
df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")

#inner join
#df_merge_inner = pd.merge(df1, df2, on="id")
print(df)
#df_removed_column = df.drop(["class"], axis=1)
df["class"] = df["class"].str.replace("Iris-","")
df = df[df["sepal_length"] > 5]
df = df[df["class"] == "virginica"]
#df.to_csv("pulsar.csv")