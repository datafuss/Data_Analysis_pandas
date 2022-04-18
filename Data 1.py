#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd


# In[65]:


df = pd.read_excel (r'C:\Users\MEDICATED ENGINEER\Desktop\pandas work\cancer-incidence-ds.xlsx')


# In[66]:


df.info()


# In[67]:


df.head()


# In[68]:


to_drop = ['Emirate Ar','Nationality Group Ar','Gender Ar']
df.drop(to_drop, inplace=True, axis=1)
df.head()


# In[69]:


new_names =  {'Emirate En': 'Emirate','Nationality Group En': 'Nationality Group','Gender En': 'Gender','Total': 'Total Deaths'}
df.rename(columns=new_names, inplace=True)
df.head()


# In[70]:


df.shape


# In[71]:


df=df.dropna()
df.shape


# In[72]:


df.dropna(how='all',axis=1,inplace=True)
df.head()


# In[73]:


#Q1: What is the total number of cancer patients died in UAE from year 2011 to 2017 ?
df['Total Deaths'].sum()


# In[74]:


#Q2:Show only those died cancer patients data who were aged between (20-29)?
df[df['Age Group'].isin(['(20-29)'])]


# In[75]:


df[df['Cancer Type'].isin(['C50 Breast'])]


# In[76]:


df.sort_values(by=['Emirate'], inplace=True)
df.head()


# In[77]:


df.sort_values(by=['Cancer Type'], inplace=True, ascending=False)
df.head()


# In[78]:


#Q Which Geo Coordinates in each Emirate has the maximium number of cancer patients?
df.groupby(['Emirate','Geo Coordinates'])['Total Deaths'].max()


# In[79]:


#Q What are the unique Cancer Types of Patients in this data set?
CancerTypes=df["Cancer Type"].unique()
print(CancerTypes)


# In[80]:


dfCancerType=df.groupby('Cancer Type').sum()
print(dfCancerType)


# In[81]:


#Q Which are the 6 cancer types with the highest number of patients died in all years and visualize the results with a bar plot?
dfCancerType.sort_values("Total Deaths", ascending=False, inplace=True)
dfCancerType.head()


# In[82]:


colors_list = ['#5cb85c','#5bc0de','#d9534f']
dfCancerType["Total Deaths"].head(6).plot.bar(figsize=(15,4),width = 0.8,color = colors_list,edgecolor=None)


# In[83]:


# Which Emirate has the maximum number of deaths due to cancer?
dfEmirate=df.groupby('Emirate').sum()
print(dfEmirate)


# In[84]:


dfEmirate.sort_values("Total Deaths", ascending=False, inplace=True)
dfEmirate.head()


# In[85]:


dfEmirate["Total Deaths"].head(6).plot.pie()


# In[86]:


dyear= df.groupby(["Year"]).sum()
dyear.head(7)


# In[87]:


#Q Whether the number of deaths decreses or increases with year? 
dyear["Total Deaths"].plot(title="Deaths causes by Cancer per year")


# In[88]:


#Q which age group is affected the most with cancers diseases?
dage= df.groupby(["Age Group"]).sum()
dage.head()


# In[89]:


dage.sort_values("Total Deaths", ascending=False, inplace=True)
dage.head()


# In[90]:


dage["Total Deaths"].plot.pie(autopct='%1.1f%%',shadow=True, startangle=90)


# In[91]:


#Q what is the ratio percentage between males and females died due to cancer?
dfGender=df.groupby('Gender').sum()
print(dfGender)


# In[92]:


df['Gender'] = df['Gender'].str.lower()


# In[93]:


dfGender=df.groupby('Gender').sum()
print(dfGender)


# In[94]:


dfGender["Total Deaths"].plot.pie(autopct='%1.1f%%',shadow=True)


# In[95]:


#Q what is the ratio percentage between Citizens and Expat died due to cancer?
dfNationality=df.groupby('Nationality Group').sum()
print(dfNationality)


# In[96]:


dfNationality["Total Deaths"].plot.pie(autopct='%1.1f%%',shadow=True)

