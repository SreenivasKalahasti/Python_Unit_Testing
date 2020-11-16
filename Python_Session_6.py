# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:54:19 2020

@author: SK5616
"""

# Loading the Pandas Package
import pandas as pd

# Creating a empty DataFrame  
df = pd.DataFrame()
print(df) 

# list of names  
names = ['John','Kumar', 'Jordon','Abraham','Mickey','Holland','Turner']

# Calling DataFrame Function on names 
namesDF = pd.DataFrame(names,columns=['Name'])

# Display the Data Frame
print(namesDF)


# Define a dictionary containing employee data
employee_data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Singapore', 'China', 'India', 'Japan'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
employeeDF= pd.DataFrame(employee_data)

# select two columns Name & Qualification
print(employeeDF[['Name', 'Qualification']])

# select columns Name,Age & Address
print(employeeDF[['Name', 'Age','Address']])


# Display the Index of the Data Frame

print(employeeDF.index)

# Inserting a new column as first coulmn into Data Frame
employeeDF.insert(loc=0, column='Id', value=[10,20,30,40])

# Inserting a new column as middle coulmn into Data Frame
employeeDF.insert(loc=2, column='Job', value=['Accountant','Manager','Admin','Engineer'])

# Inserting a new column as last coulmn into Data Frame
employeeDF.insert(loc=len(employeeDF.columns), column='Salary', value=[3400,2700,1700,4300])

# Insert row into the Data Frame

new_row = {'Id':50,'Name':'George', 'Job':'Data Scientist','Age':31, 'Address':'Hongkong', 'Qualification':'MBA','Salary':5000}

employeeDF = employeeDF.append(new_row,ignore_index=True)

new_row = {'Id':51,'Name':'Andrew', 'Job':'Engineer','Age':32, 'Address':'China', 'Qualification':'MBA','Salary':2700}
employeeDF = employeeDF.append(new_row,ignore_index=True)
new_row = {'Id':52,'Name':'Jay', 'Job':'Manager','Age':29, 'Address':'Singapore', 'Qualification':'MCA','Salary':4300}
employeeDF = employeeDF.append(new_row,ignore_index=True)

# Display the size of Data Frame
print(employeeDF.shape)

# Describe the Dara Frame
print(employeeDF.describe())

# Display the Data Types of Columns
print(employeeDF.dtypes)

# Display the top N rows
print(employeeDF.head(3))

# Display bottom N rows
print(employeeDF.tail(2))

# Display Unique values in the Data Frame
print(employeeDF.nunique())


# Display Unique values in the Data Frame
print(employeeDF['Job'].value_counts())

print(employeeDF['Age'].value_counts())

# Display the column names in the Data Frame
print(employeeDF.columns)

# Display the values in the Data Frame
print(employeeDF.values)

# Confirm Rows between two values from Data Frame
print(employeeDF['Age'].between(20,30))

print(employeeDF[employeeDF['Age'].between(20,30)])

print(employeeDF[employeeDF['Age'].between(20,30)==True])

print(employeeDF[employeeDF['Age'].between(20,30)==False])

# Display data based on row index
print(employeeDF.loc[2:4])
print(employeeDF.iloc[3:5])

# Display the row which contain the least 3 values in the column
print(employeeDF.nsmallest(3,'Age'))

# Display the row which contain the top 3 Ages in the column
print(employeeDF.nlargest(3,'Age'))

# Display the databased on Rank order
print(employeeDF['Age'].rank())

# sorting w.r.t name column 
employeeDF.sort_values("Age", inplace = True)

# Display the databased on Rank order
print(employeeDF)