#!/usr/bin/env python
# coding: utf-8

# ## Task 3

# ### Problem 1: Polar Coordinates

# In[69]:


import cmath
num=complex(input().strip())
print(cmath.polar(num)[0])
print(cmath.polar(num)[1])


# ### Problem 2: Find angle MBC

# In[77]:


from math import*
AB=float(input())
BC=float(input())
print(str(int(round(degrees(atan(AB/BC)),0)))+'°')


# ### Problem 3: Triangle Quest 2

# In[82]:


for i in range(1,int(input())+1):
    print((10**i//9)**2)


# ### Problem 4: Mod Divmod

# In[83]:


a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))


# ### Problem 5: Power - Mod Power

# In[84]:


a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))


# ### Problem 6: Integers come in all sizes

# In[85]:


a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))


# ### Function 7: Triangle quest

# In[88]:


for i in range(1,int(input())):
    print(str(i)*i)


# In[ ]:




