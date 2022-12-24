# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:59:00 2022

@author: Vaishu
"""
import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
#Reading the csv file in pandas

df=pd.read_csv(r"C:\Users\Vaishu\Desktop\Work\project_01\education_COVID-19__.csv")
print(df.head(200))
# Deatils of the data frame
print(df.shape)
print(df.describe())
print(df.columns)
#Dealing with the date format
df['If Closed Due To COVID19 When'] = pd.to_datetime(df['If Closed Due To COVID19 When'], errors='coerce')
df['If Closed Due To COVID19 When'] = df['If Closed Due To COVID19 When'].replace(np.nan, 0)
print(df)

# Replacing commas with ''

df1=df.replace(",","",regex=True) #converting comma(,) to ()



#%%
# checking on data type
for column in df1.columns:
    print(df1[column].dtype)
    
#Deleting some columns    
df2 = df1.drop(labels=["Latitude", "Longitude","Year Pre", "Year Prm", "Year Sec", "Year Ter"], axis=1)
print(df2)

print(df2.columns)    

#%%
#converting non numeric values to numeric values
    
df2[["Enrollment", "Se Pre Enrl","Se Sec Enrl","Se Prm Enrl","Se Ter Enrl"]] = df2[["Enrollment", "Se Pre Enrl","Se Sec Enrl","Se Prm Enrl","Se Ter Enrl"]].apply(pd.to_numeric)
  
#replacing NaN values to median 
    
df3=df2.fillna({'Enrollment': df2['Enrollment'].median(),
            'Se Pre Enrl': df2['Se Pre Enrl'].median(),
            'Se Sec Enrl': df2['Se Sec Enrl'].median(),
            'Se Prm Enrl': df2['Se Prm Enrl'].median(),
            'Se Ter Enrl': df2['Se Ter Enrl'].median()})
            


#%%
#printing unique values in all the column
       
for values in df3:
    print("{} has {} values.They are:".format(values,len(df3[values].unique()))) 
    print(df3[values].unique())
    print('\n')
    
#%% getting number of missing data in each column    
print(df3.isna().sum())
# Handling the missing data
index_with_nan = df3.index[df3.isnull().any(axis=1)]
print( index_with_nan)
print(df3)
#%%
#Filling the missing numerical data with median

df4=df3.replace(",","",regex=True)     
df4[['Enrollment', 'Se Pre Enrl', 'Se Prm Enrl','Se Sec Enrl', 'Se Ter Enrl']]=df4[['Enrollment', 'Se Pre Enrl', 'Se Prm Enrl','Se Sec Enrl', 'Se Ter Enrl']].apply(pd.to_numeric)     
     
df4=df3.fillna(df3.median()) 
print(df4)
#Renaming the columns in df4
df4.rename(columns={'Country Name':'country_name','Se Pre Enrl': 'Pre_enrl', 'Se Prm Enrl': 'Prm_enrl','Se Sec Enrl':'Sec_enrl','Se Ter Enrl':'Ter_enrl'}, inplace=True)

print(df4)
print(df4.columns)
#%%
df4.loc[df4['Enrollment'].idxmax()]
df4.loc[df4['Enrollment'].idxmin()]

#%%
#ploting the graph country vs  enrollments in pri primary uning pandas

df4.iloc[:50].plot.bar(x='country_name', y='Pre_enrl')
plt.rcParams["figure.dpi"]=120
plot=df4.plot.bar(x='country_name', y='Pre_enrl',figsize=(50,20))
fig=plot.get_figure()
fig.savefig("output1.png")

#%%

ax = sns.barplot(x="country_name", y="Pre_enrl", data=df4)

#%%
#ploting the graph country vs total number of enrollments  uning pandas

df4.iloc[:50].plot.bar(x='country_name', y='Enrollment')
plt.rcParams["figure.dpi"]=120
plot=df4.plot.bar(x='country_name', y='Enrollment',figsize=(50,30))
fig=plot.get_figure()
fig.savefig("output2.png")
#%%

#ploting the graph country vs  enrollments in primary uning pandas

df4.iloc[:50].plot.bar(x='country_name', y='Prm_enrl')
plt.rcParams["figure.dpi"]=120
plot=df4.plot.bar(x='country_name', y='Prm_enrl',figsize=(40,10))
fig=plot.get_figure()
fig.savefig("output3.png")
#%%
#ploting the graph country vs  enrollments in secondary uning pandas

df4.iloc[:50].plot.bar(x='country_name', y='Sec_enrl')
plt.rcParams["figure.dpi"]=120
plot=df4.plot.bar(x='country_name', y='Sec_enrl',figsize=(40,10))
fig=plot.get_figure()
fig.savefig("output4.png")
#%%
#ploting the graph country vs  enrollments in tertiary uning pandas

df4.iloc[:50].plot.bar(x='country_name', y='Ter_enrl')
plt.rcParams["figure.dpi"]=120
plot=df4.plot.bar(x='country_name', y='Ter_enrl',figsize=(40,10))
fig=plot.get_figure()
fig.savefig("output5.png")


#%% study on enrollements in Europe and Central Asia

df_europe = df4[df4["Region Name"]=="Europe and Central Asia"][["Enrollment","country_name"]]
print(df_europe)
print(df_europe.describe())
print(df_europe.shape)

plot=df_europe.plot.bar(x='country_name', y='Enrollment',figsize=(10,2))

 
#%%
#comparing Income level with Enrollment

ax=sns.countplot(x="Income Level",hue="Region Name",data=df4,order=["Low income","Lower middle income","Upper middle income","High income"])
plt.legend(loc="best", frameon=True)
plt.show()

#%%

ax = df4.plot.hist(column=["School Status"], by="country_name", figsize=(20, 10))

df_status = DataFrame(np.random.randn(500).reshape(100,5), column=list('School Status'))
axes = df_status.hist(sharey=True, sharex=True)
pl.suptitle("This is Figure title")
#%%
#comparison on country and Enrollments

sns.relplot(x="country_name", y="Enrollment", kind="scatter", data=df4);
#%%
#split Apply Combine
#Grouped by Region name 
g = df4.groupby("Region Name")
print(g)


for region, y in g:
    print("Region Name:",region)
    print("\n")
    print("data:",y)  
df_region=g.mean()
print(df_region)


#%%
df_region[['Pre_enrl','Prm_enrl','Sec_enrl','Ter_enrl']].plot.barh(stacked =True)
plt.legend(ncol=2, loc="best", frameon=True)
plt.xlabel("Enrollments")
plt.show()



#%%
i=df4.groupby("Income Level")
print(i)


for income, x in i:
    print("Income Level:",income)
    print("\n")
    print("data:",x)  
df_income=i.mean()
print(df_income)


#%% comparision of Enrollments ion the basis of Income

df_income[['Pre_enrl','Prm_enrl','Sec_enrl','Ter_enrl']].plot.barh(stacked =True)
plt.legend(ncol=2, loc="best", frameon=True)
plt.xlabel("Enrollments")
plt.show()


#%%
#comparision of status of the schools in different region during the pandemic

df4['If Closed Due To COVID19 When']=df4['If Closed Due To COVID19 When'].astype('string')

df4['COUNTER'] =1
df_status = df4.groupby(["If Closed Due To COVID19 When","School Status","Region Name"])['COUNTER'].sum() #sum function
print(df_status)



fig = plt.gcf()

# Change seaborn plot size
fig.set_size_inches(15, 4)
sns.scatterplot(data=df_status, x="If Closed Due To COVID19 When", y="Region Name",hue="School Status",s=80)
plt.legend(loc="lower right", frameon=True)
plt.rcParams["figure.dpi"]=120
plt.xticks(rotation =90)
plt.show()




