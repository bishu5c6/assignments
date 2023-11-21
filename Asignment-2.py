#!/usr/bin/env python
# coding: utf-8

# In[4]:


rows=9
for i in range(rows):
    for j in range(i+1):
        print('* ',end='')
    print()


# In[5]:


rows=9
for i in range(rows):
    for j in range(i,rows):
        print('* ',end='')
    print()


# In[7]:


rows = 9
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")



for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# In[ ]:


a=input("Enter the word: ")
print(a[::-1])

