#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


google_data=pd.read_csv('googleplaystore.csv')


# In[3]:


google_data.head()  #top 5 rows


# In[4]:


google_data.tail()  #last 5 rows


# In[5]:


google_data.shape  #Number of rows and columns


# In[6]:


google_data.describe()  #Summary


# In[7]:


google_data.boxplot()


# In[8]:


google_data.hist()


# In[9]:


google_data.info()


# In[10]:


google_data.isnull()


# In[11]:


google_data.isnull().sum()    #Counting the null values in each column


# ## Checkingh the Outliers - Apps having ratings > 5

# In[12]:


google_data[google_data.Rating > 5]


# In[13]:


#droppping the outlier 
google_data.drop([10472],inplace=True)


# In[14]:


#Checking if the row has deleted
google_data[10470:10475]


# In[15]:


google_data.boxplot()


# In[16]:


google_data.hist()


# ## Checking for columns hacve scarcity of data, i.e. >90%
# 

# In[17]:


threshold=len(google_data)*0.1
threshold


# In[18]:


google_data.dropna(thresh=threshold,axis=1,inplace=True)


# In[19]:


print(google_data.isnull().sum())


# In[20]:


google_data.shape


# # Data Imputation and Manupulation

# Filling the null values with Mean,Median,Mode

# In[21]:


def impute_median(series):
    return series.fillna(series.median())


# In[22]:


google_data.Rating=google_data['Rating'].transform(impute_median)


# In[23]:


google_data.isnull().sum()


# In[24]:


#Alternate Method
"mean=google_data['Rating'].median"
'mean'
"google_data['Rating']=google_data['Rating'].fillna(median)"


# In[25]:


#Missing value  tretemnet for Categorical features
print(google_data['Type'].mode())
print(google_data['Current Ver'].mode())
print(google_data['Android Ver'].mode())


# In[26]:


#Filling the missing values with mode
google_data['Type'].fillna(str(google_data['Type'].mode().values[0]),inplace=True)
google_data['Current Ver'].fillna(str(google_data['Current Ver'].mode().values[0]),inplace=True)
google_data['Android Ver'].fillna(str(google_data['Android Ver'].mode().values[0]),inplace=True)


# In[27]:


#Check for the tretment 
google_data.isnull().sum()


# In[28]:


#lets conver Price,Reviews and ratings data into Numerical Values
google_data['Price']=google_data['Price'].apply(lambda x : str(x).replace('$', '') if '$' in str(x) else str(x))
google_data['Price']=google_data['Price'].apply(lambda x: float(x))
google_data['Reviews']=pd.to_numeric(google_data['Reviews'],errors='coerce')


# In[29]:


google_data['Installs']=google_data['Installs'].apply(lambda x : str(x).replace('+','')if '+' in str(x) else str(x))
google_data['Installs']=google_data['Installs'].apply(lambda x : str(x).replace(',','')if ',' in str(x) else str(x))
google_data['Installs']=google_data['Installs'].apply(lambda x:float(x))


# In[30]:


google_data.head(10)


# In[31]:


google_data.describe()  # After cleaning data


# ### Data Visulaisation 
# 

# In[32]:


grp = google_data.groupby('Category')
x=grp['Rating'].agg(np.mean)
y=grp['Price'].agg(np.sum)
z=grp['Reviews'].agg(np.mean)
print(x)
print(y)
print(z)


# In[35]:


#Plotting the Ratings data in a Graph
plt.figure(figsize=(15,7))
plt.plot(x,'ro',color='b')
plt.xticks(rotation=90)
plt.title('Category Wise Rating')
plt.xlabel('Categories')
plt.ylabel('Rating')
plt.show()


# From the above graph its is infered that Education and Family apps have received the highest ratings where as Dating, Maps and Tolls apps have received the lowest ratings.

# In[36]:


#Plotting the Price data in a Graph
plt.figure(figsize=(15,7))
plt.plot(y,'r--',color='r')
plt.xticks(rotation=90)
plt.title('Category Wise Pricing')
plt.xlabel('Categories')
plt.ylabel('RPrice')
plt.show()


# From the above Graph it is visible that the Family, Finance, Lifestyle,and Medical apps have the highest prices where as Art and Design, Weather, Dating, Libraries apps have lowest prices.

# In[37]:


#Plotting the Reviews data in a Graph
plt.figure(figsize=(15,7))
plt.plot(z,'ro',color='b')
plt.xticks(rotation=90)
plt.title('Category Wise Reviews')
plt.xlabel('Categories')
plt.ylabel('Reviews')
plt.show()


# From the above graph it is infered that the Communication, Social and Games apps have the highest number of reviews wheres as Beauty ,Events, Art and Design,Medical have the lowest number of reviews.
