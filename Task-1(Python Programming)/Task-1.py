#!/usr/bin/env python
# coding: utf-8

# ## Task 1

# ### Problem 1: Print 'Hello World'

# In[1]:


print("Hello, World!")


# ### Problem 2: If-else

# In[2]:


n=int(input())
if n%2!=0:
    print("Weird")
else:
    if n in range(2,6) or n>20:
        print("Not Weird")
    elif n in range(6,21):
        print('Weird')        
    


# ### Problem 3: Arithmetic Operators

# In[3]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# ### Problem 4: Division

# In[4]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# ### Problem 5: Loops

# In[5]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)


# ### Problem 6: Function

# In[6]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap=True    
    
    return leap

year = int(input())
print(is_leap(year))


# ### Function 7: Function

# In[7]:


if __name__ == '__main__':
    s=""
    n = int(input())
    for i in range(1,n+1):
        i=str(i)
        s+=i
    
    print(s)    

