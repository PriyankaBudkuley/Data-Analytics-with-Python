#!/usr/bin/env python
# coding: utf-8

# # Assignment \#3 - the Facebook dataset 2/2
# 
# Exploratory Data Analysis giving insights from the Facebook dataset.
# 
# Source: http://www.kaggle.com
# 
# **Features description**
# - *userid*: anonymized user id
# - *age*: age in years
# - *dob_day*: date of birth (day)
# - *dob_year*: date of birth (year)
# - *dob_month*: date of birth (month)
# - *gender*: gender
# - *tenure*: number of days in Facebook
# - *friend_count*: number of friends
# - *friendships_initiated*: number of friends initiated
# - *likes*: number of likes performed
# - *likes_received*: number of likes received
# - *mobile_likes*: number of mobile likes performed
# - *mobile_likes_received*: number of mobile likes received
# - *www_likes*: number of web likes performed
# - *www_likes_received*: number of web likes received

# #### Checklist before submitting your assignment:
# - Check individually each function by invoking it.
# - Check that functions which return floating point number, you round them to 1 decimal point.
# - Clean up your notebook before exporting it to Python format: remove unnecessary cells where you performed tests...
# - Check that the Python file do not contain any syntax error:
#     * Open a command window and type: <pre>python assignment_3.py</pre>
#     * Or copy paste the whole content of your Python file into a cell of your notebook and run it
#     * No error should be output!
# - Upload your file in the Google drive folder and check that the name of the file is appropriate, with no extra character, here: `assignment_3.py`

# **Questions**
# 
# Load the dataset and answer to all questions by implementing a function with no arguments.
# 
# The dataset should be saved and unzip along with your notebook.
# 
# The different functions should use one of the variables that have been defined below and perform the appropriate computation.
# 
# Many questions deal with differences between females and males in the dataset.
# Therefore, we have computed and prepared 3 datasets which are to be used:
# - `df`: whole dataset,
# - `df_female`: dataset with females only,
# - `df_male`: dataset with males only.
# 
# **Caution**: Questions asking to return a floating point number (mean, percentage) should round it to 1 decimal place:
# - Such questions are marked with `(°)`.
# - For instance, if the variable `result` is a floting point number, e.g. `3.14159265359`
# - The function should return `round(result, 1)` instead of `result`, e.g. `3.1`
# - Percentages should be returned as floating point numbers and not with the `%` mark.
# 
# **Tip**: All questions might be answered without implementing any loop nor any if/else statement.
# 
# **Percentage who did not performed any like (°)**
# 
# 1) What is the percentage of females who did not performed any like (°)?
# 
# 2) What is the percentage of males who did not performed any like (°)?
# 
# **Percentage who did not received any like (°)**
# 
# 3) What is the percentage of females who did not received any like (°)?
# 
# 4) What is the percentage of males who did not received any like( °)?
# 
# **Percentage of mobile likes performed compared to all likes performed (°)**
# 
# 5) What is the percentage of mobile likes performed by females compared to all likes performed by females (°)?
# 
# 6) What is the percentage of mobile likes performed by males compared to all likes performed by males (°)?
# 
# **Percentage of mobile likes received compared to all likes received (°)**
# 
# 7) What is the percentage of mobile likes received by females compared to all likes received by females (°)?
# 
# 8) What is the percentage of mobile likes received by males compared to all likes received by males (°)?
# 
# **Most frequent age**
# 
# 9) What is the most frequent age of all users?
# 
# **Friendship vs friendships initiated (°)**
# 
# 10) What is the mean of the difference between friend count and friendships initiated for females (°)?
# 
# 11) What is the mean of the difference between friend count and friendships initiated for males (°)?
# 
# **Months and days of the given date of birth (°)**
# 
# The last 4 questions deal with the months and days used by Facebook users for their date of birth.
# 
# The idea is that people do not give their actual date of birth. They often switch the actual month to Januray and the actual day to the first day of a month.
# 
# The percentage of people being born in January is *circa* $100 \times \frac{1}{12}$ since there are 12 months in a year.
# 
# We are going to compute the difference between the percentage found in the dataset and this theorical percentage.
# 
# 12) What is the difference between the percentage of females born in January and 100/12 (°)?
# 
# 13) What is the difference between the percentage of males born in January and 100/12 (°)?
# 
# The percentage of people being born the first day of a month is *circa* $100 \times \frac{12}{365}$ since there are 12 days which are the first day of a month in a year and there are 365 days in a year (forget the leap years).
# 
# We are going to compute the difference between the percentage found in the dataset and this theorical percentage.
# 
# 14) What is the difference between the percentage of females born the first day of a month and 1200/365 (°)?
# 
# 15) What is the difference between the percentage of males born the first day of a month and 1200/365 (°)?
# 
# (°) Result of functions should be rounded to 1 decimal place.
# 
# **Now you have a better view of some differences between female and male Facebook users!**

# In[1]:


# usual import and options
import pandas as pd
pd.set_option("display.min_rows", 16)
pd.set_option("display.max_columns", 30)


# In[2]:


# DO NOT MODIFY THIS CELL
# MAKE SURE THAT THE FILE 'pseudo_facebook.csv' IS ALONG WITH THE DATASET 'pseudo_facebook.csv'
# USE THE 3 VARIABLES: df, df_female, df_male IN YOUR FUNCTIONS
# ALL FUNCTIONS SHOULD HAVE NO ARGUMENT

# load the dataset and build subsets with females and males
df = pd.read_csv('pseudo_facebook.csv')
df_female = df.loc[df['gender'] == 'female']
df_male = df.loc[df['gender'] == 'male']
df.head()


# In[3]:


# 1) What percentage of females did not performed any like (°)?
def exercise_01():
    result =(df_female.loc[(df_female['likes'] == 0)].count() / df_female.count())*100
    return round(result["likes"], 1)

# run and check
exercise_01()


# In[4]:


# 2) What percentage of males did not performed any like (°)?
def exercise_02():
    result = (df_male.loc[(df_male['likes'] == 0)].count() / df_male.count())*100
    return round(result["likes"], 1)

# run and check
exercise_02()


# In[5]:


# 3) What percentage of females did not received any like (°)?
def exercise_03():
    result = (df_female.loc[(df_female['likes_received'] == 0)].count() / df_female.count())*100
    return round(result["likes_received"], 1)

# run and check
exercise_03()


# In[6]:


# 4) What percentage of males did not received any like (°)?
def exercise_04():
    result = (df_male.loc[(df_male['likes_received'] == 0)].count() / df_male.count())*100
    return round(result["likes_received"], 1)

# run and check
exercise_04()


# In[7]:


# 5) What is the percentage of mobile likes performed by females compared to all likes performed by females (°)?
def exercise_05():
    result = (df_female['mobile_likes'].sum() / df_female['likes'].sum())*100
    return round(result, 1)

# run and check
exercise_05()


# In[8]:


# 6) What is the percentage of mobile likes performed by males compared to all likes performed by males (°)?
def exercise_06():
    result = (df_male['mobile_likes'].sum() / df_male['likes'].sum())*100
    return round(result, 1)

# run and check
exercise_06()


# In[9]:


# 7) What is the percentage of mobile likes received by females compared to all likes received by females (°)?
def exercise_07():
    result = (df_female['mobile_likes_received'].sum() / df_female['likes_received'].sum())*100
    return round(result, 1)

# run and check
exercise_07()


# In[10]:


# 8) What is the percentage of mobile likes received by males compared to all likes received by males (°)?
def exercise_08():
    result = (df_male['mobile_likes_received'].sum() / df_male['likes_received'].sum())*100
    return round(result, 1)

# run and check
exercise_08()


# In[11]:


# 9) What is the most frequent age of users?
def exercise_09():
    result = df["age"].value_counts().idxmax()
    return result

# run and check
exercise_09()


# In[12]:


# 10) What is the mean of the difference between friend count and friendships initiated for females (°)?
def exercise_10():
    result = df_female["friend_count"].mean() - df_female["friendships_initiated"].mean()
    return round(result, 1)

# run and check
exercise_10()


# In[13]:


# 11) What is the mean of the difference between friend count and friendships initiated for males (°)?
def exercise_11():
    result = df_male["friend_count"].mean() - df_male["friendships_initiated"].mean()
    return round(result, 1)

# run and check
exercise_11()


# In[14]:


# 12) What is the difference between the percentage of females born in January and 100/12 (°)?
def exercise_12():
    result =  ((df_female.loc[(df_female["dob_month"]==1)].count()/df_female["dob_month"].count())*100)-100/12
    return round(result["dob_month"], 1)

# run and check
exercise_12()


# In[15]:


# 13) What is the difference between the percentage of males born in January and 100/12 (°)?
def exercise_13():
    result = ((df_male.loc[(df_male["dob_month"]==1)].count()/df_male["dob_month"].count())*100)-100/12
    return round(result["dob_month"], 1)

# run and check
exercise_13()


# In[16]:


# 14) What is the difference between the percentage of females born the first of a month and 1200/365 (°)?
def exercise_14():
    result = ((df_female.loc[(df_female["dob_day"]==1)].count()/df_female["dob_day"].count())*100)-1200/365
    return round(result["dob_month"], 1)

# run and check
exercise_14()


# In[17]:


# 15) What is the difference between the percentage of males born the first of a month and 1200/365 (°)?
def exercise_15():
    result = ((df_male.loc[(df_male["dob_day"]==1)].count()/df_male["dob_day"].count())*100)-1200/365
    return round(result["dob_month"], 1)

# run and check
exercise_15()


# In[ ]:




