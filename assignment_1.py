#!/usr/bin/env python
# coding: utf-8

# # Assignment \#1 - the Python beginner
# 
# 0) Create a function which computes the area of a rectangle given its height and width. Example: given 10 and 20, should return 200.
# 
# 1) Create a function which given 2 booleans computes the exclusive OR (should return True if one boolean is True and the other boolean is False; and False if both booleans are True or both booleans are False). Example: given True and False, should return True.
# 
# 2) Create a function which given hours, minutes and seconds computes the total number of seconds. Example: given 1 hour, 1 minute and 1 second, should return 3661.
# 
# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included. Example: given 3, should return 18 (3 + 4 + 5 + 6).
# 
# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one. If the initial string is empty, it should return an empty string. Example: given 'Python', should return 'Pn'.
# 
# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y:' where X is the initial string and Y is the reverse of the initial string. Example: given 'Paris', should return 'The reverse of Paris is siraP:'.
# 
# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise. Example: given 'Python', should return True; and given 'alphabet', should return False.
# 
# 7) Create a function which given a string returns True if the string is a palindrome (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise. Example, given 'tattarrattat', should return True; and given 'alphabet', should return False.
# 
# 8) Create a function which given 3 numbers returns the one which is in the middle. Example: given 9, 5 and 6, should return 6.
# 
# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'Hello'.
# 
# 10) Create a function which given a list of strings returns the longest one. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'elephants'.

# In[1]:


# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# 0) Create a function which computes the area of a rectangle given its height and width.
def exercise_00(height, width):
    result = height * width
    return result


# In[2]:


# run and check
exercise_00(10, 20)


# In[3]:


# 1) Create a function which given 2 booleans computes the exclusive OR.
# (should return True if one boolean is True and the other boolean is false, False if both booleans are True or both booleans are False).
# change the line 'result = None' to perform the appropriate calculation
def exercise_01(bool1, bool2):
 if exercise_01 == (True, False) or (False, True):
    print(True)
 else:
    exercise_01 == (True, True) or (False, False)
    print(False)


# In[4]:


# run and check
exercise_01(True, False)


# In[5]:


# 2) Create a function which given hours, minutes and seconds computes the total of seconds.
# change the line 'result = None' to perform the appropriate calculation
def exercise_02(hours, minutes, seconds): 
 result = (hours*3600) + (minutes*60) + (seconds*seconds)
 return result


# In[6]:


# run and check
exercise_02(1, 1, 1)


# In[7]:


# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included.
# change the line 'result = None' to perform the appropriate calculation
def exercise_03(integer):
 result = int((integer+1)*(integer+(integer+integer))/2)
 return result


# In[8]:


# run and check
exercise_03(3)


# In[9]:


# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one.
# If the initial string is empty, it should return an empty string.
    # change the line 'result = None' to perform the appropriate calculation
def exercise_04(string):
 if len(string)==0:
  result=("")
 else:
  result=(string[0]+string[-1])
 return result


# In[10]:


# run and check
exercise_04("Python")


# In[11]:


# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y:'
# change the line 'result = None' to perform the appropriate calculation
def exercise_05(string):
 s=""
 for i in s:
    str=i + str
    return str
 print("The reverse of", string, "is", string[::-1])


# In[12]:


# run and check
exercise_05('Paris')


# In[13]:


# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise.
 # change the line 'result = None' to perform the appropriate calculation
def exercise_06(string):
 string = string.lower()
 for c in string:
        if string.count(c) != 1:
            return False
        return True


# In[14]:


# run and check
exercise_06('Python')


# In[15]:


# 7) Create a function which given a string returns True if the string is a palindrome
# (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise.
 # change the line 'result = None' to perform the appropriate calculation
def exercise_07(string):
 if (string)==string[::-1]:
  result = True
 else:
  result= False
 return result


# In[16]:


# run and check
exercise_07('tattarrattat')


# In[17]:


# 8) Create a function which given 3 numbers returns the one which is in the middle.
# change the line 'result = None' to perform the appropriate calculation
def exercise_08 (number1, number2, number3):
 if number1>number2 and number1<number3:
    return number1
 if number2>number1 and number2<number3:
    return number2
 return number3


# In[18]:


# run and check
exercise_08(9, 5, 6)


# In[19]:


# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list.
# change the line 'result = None' to perform the appropriate calculation
def exercise_09(list_of_strings):
 result = list(filter(lambda item: item.strip(), list_of_strings))
 return result


# In[20]:


# run and check
exercise_09(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# In[21]:


# 10) Create a function which given a list of strings returns the longest one.
# change the line 'result = None' to perform the appropriate calculation
def exercise_10(list_of_strings):
 result=(max(list_of_strings,key=len))
 return result


# In[22]:


# run and check
exercise_10(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# In[ ]:




