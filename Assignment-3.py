#!/usr/bin/env python
# coding: utf-8

# ## by the help of reduce function we use a list or iterable into one

# ### reduce() = apply a function to an iterable and reduce it to a single cumulative values.performs on first two elements and repeat process until 1 value remains

# In[4]:


#reduce(function, iterable)


# In[5]:


import functools
l=['b','i','s','w','a','n','t','h']
word = functools.reduce(lambda x,y:x+y,l)


# In[6]:


print(word)


# In[7]:


number = (1,2,3,4,5)
on=functools.reduce(lambda x,y:x*y,number)
print(on)


# In[21]:


import functools
def add(a,b):
    return a*b
#above is the function
#now creating a iterable object
num_list=[1,2,3,4,5,6,7,8,9,10]
sums=functools.reduce(add,num_list)
print(f"The multiplication of all the numbers is:{sums} ")


# In[24]:


# Same Solution can be approached by Built-in reduce() function

print("Input:")
number=int(input("Please insert the number :"))

num_list= list(range(1,(number+1)))
# Import reduce function 

sum_of_elements =functools.reduce((lambda x, y: x + y), num_list)

#Output
print("Output:")
print("List of First n Natural numbers are:",num_list)
print("Sum of List elements are :",sum_of_elements)


# In[26]:


print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))

num_even_list=list(filter(lambda x: x%2==0,list(filter(lambda x: x%5==0 ,num_list))))
num_odd_list= list(filter(lambda x: x%2!=0,list(filter(lambda x: x%5==0 ,num_list))))

print("Output:")

print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",num_even_list)
print("List of Odd numbers, which are multiples of 5 are:",num_odd_list)


# In[ ]:





# In[22]:


#Solution

#Section 1
word="AcadGild"
#list Comprehension
output_list=[w.upper() for w in list(word)]
print("Output:")
print(output_list)

#Section 2
word_1=list('xyz')
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

#Section 3
word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

#Section 4
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

#Section 5
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

#Section 6
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)


# In[ ]:




