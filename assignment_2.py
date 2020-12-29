#!/usr/bin/env python
# coding: utf-8

# # Assignment \#2 - the Facebook dataset 1/2
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
#     * Open a command window and type: <pre>python assignment_2.py</pre>
#     * Or copy paste the whole content of your Python file into a cell of your notebook and run it
#     * No error should be output!
# - Upload your file in the Google drive folder and check that the name of the file is appropriate, with no extra character, here: `assignment_2.py`

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
# **General questions**
# 
# 0) How many rows does the whole DataFrame have?
# 
# 1) How many columns does the whole DataFrame have?
# 
# **Females and males**
# 
# 2) How many females are there in the dataset?
# 
# 3) How many males are there in the dataset?
# 
# **Total number of likes performed**
# 
# 4) What is the total number of likes performed by females?
# 
# 5) What is the total number of likes performed by males?
# 
# **Total number of likes received**
# 
# 6) What is the total number of likes received by females?
# 
# 7) What is the total number of likes received by males?
# 
# **Mean age (°)**
# 
# 8) What is the mean age of females (°)?
# 
# 9) What is the mean age of males (°)?
# 
# **Mean friend count (°)**
# 
# 10) What is the mean friend count of females (°)?
# 
# 11) What is the mean friend count of males (°)?
# 
# **Mean number of likes performed (°)**
# 
# 12) What is the mean number of likes performed by females (°)?
# 
# 13) What is the mean number of likes performed by males (°)?
# 
# **Mean number of likes received (°)**
# 
# 14) What is the mean number of likes received by females (°)?
# 
# 15) What is the mean number of likes received by males (°)?
# 
# (°) Result of functions should be rounded to 1 decimal place.

# In[1]:


# usual import and options
import pandas as pd
pd.set_option("display.max_rows", 16)
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


# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# ALL FUNCTIONS SHOULD FOLLOW THE SAME PATTERN:
# - DEFINITION OF THE FUNCTION: def exercise_XX():
# - COMPUTATION OF THE RESULT: result = ...
# - RETURN OF THE RESULT: return result

# 0) How many rows does the dataFrame have?
def exercise_00():
    result = len(df)
    return result

# run and check
exercise_00()


# In[4]:


# 1) How many columns does the DataFrame have?
def exercise_01():
    result = len(df.columns)
    return result

# run and check
exercise_01()


# In[5]:


# 2) How many females are there in the dataset?
def exercise_02():
    result = len(df_female)
    return result

# run and check
exercise_02()


# In[6]:


# 3) How many males are there in the dataset?
def exercise_03():
    result = len(df_male)
    return result

# run and check
exercise_03()


# In[7]:


# 4) What is the total number of likes performed by females?
def exercise_04():
    result = df_female['likes'].sum()
    return result

# run and check
exercise_04()


# In[8]:


# 5) What is the total number of likes performed by males?
def exercise_05():
    result = df_male['likes'].sum()
    return result

# run and check
exercise_05()


# In[9]:


# 6) What is the total number of likes received by females?
def exercise_06():
    result = df_female['likes_received'].sum()
    return result

# run and check
exercise_06()


# In[10]:


# 7) What is the total number of likes received by males?
def exercise_07():
    result = df_male['likes_received'].sum()
    return result

# run and check
exercise_07()


# In[11]:


# 8) What is the mean age of females (°)?
def exercise_08():
    result = df_female['age'].mean()
    return round(result, 1)

# run and check
exercise_08()


# In[12]:


# 9) What is the mean age of males (°)?
def exercise_09():
    result = df_male['age'].mean()
    return round(result, 1)

# run and check
exercise_09()


# In[13]:


# 10) What is the mean friend count of females (°)?
def exercise_10():
    result = df_female['friend_count'].mean()
    return round(result, 1)

# run and check
exercise_10()


# In[14]:


# 11) What is the mean friend count of males (°)?
def exercise_11():
    result = df_male['friend_count'].mean()
    return round(result, 1)

# run and check
exercise_11()


# In[15]:


# 12) What is the mean number of likes performed by females (°)?
def exercise_12():
    result = df_female['likes'].mean()
    return round(result, 1)

# run and check
exercise_12()


# In[16]:


# 13) What is the mean number of likes performed by males (°)?
def exercise_13():
    result = df_male['likes'].mean()
    return round(result, 1)

# run and check
exercise_13()


# In[17]:


# 14) What is the mean number of likes received by females (°)?
def exercise_14():
    result = df_female['likes_received'].mean()
    return round(result, 1)

# run and check
exercise_14()


# In[18]:


# 15) What is the mean number of likes received by males (°)?
def exercise_15():
    result = df_male['likes_received'].mean()
    return round(result, 1)

# run and check
exercise_15()


# In[ ]:




