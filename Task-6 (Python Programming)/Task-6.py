#!/usr/bin/env python
# coding: utf-8

# ## Task - 6

# ### Function 1: Array

# In[17]:


import numpy
def arrays(arr):
    a=numpy.array(arr,float)
    return a[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# ### Function 2: Shape and Reshape

# In[18]:


import numpy
def reshape(arr):
    a=numpy.array(arr,int)
    return numpy.reshape(a,(3,3))
arr=input().strip().split(' ')
result=reshape(arr)
print(result)    


# ### Function 3: Transpose and Flatten

# In[4]:


import numpy
N, M = list(map(int, input().split()))
a = numpy.array([input().split() for _ in range(N)], int)
print(a.transpose())
print(a.flatten())


# ### Function 4: Concatenate

# In[5]:


import numpy
N,M,P=list(map(int,input().split()))
arr1=numpy.array([input().split() for i in range(N)],int)
arr2=numpy.array([input().split() for j in range(M)],int)
print(numpy.concatenate((arr1,arr2),axis=0))


# ### Function 5: Zeros and ones

# In[6]:


import numpy
num=list(map(int,input().split()))
print(numpy.zeros(num,dtype=numpy.int))
print(numpy.ones(num,dtype=numpy.int))


# ### Function 6: Eye and Identity

# In[ ]:


import numpy
N,M=list(map(int,input().split()))
numpy.set_printoptions(sign=' ')
print(numpy.eye(N,M))


# ### Function 7: Array Mathematics

# In[8]:


import numpy
N,M=list(map(int,input().split()))
A=numpy.array([input().split() for _ in range(N)],int)
B=numpy.array([input().split() for _ in range(N)],int)
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(A//B)
print(numpy.mod(A,B))
print(numpy.power(A,B))


# ### Function 8: Floor , ceil and Rint

# In[10]:


import numpy
arr=input().strip().split(' ')
a=numpy.array(arr,float)
numpy.set_printoptions(sign=' ')
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# ### Function 9: Sum and Prod

# In[12]:


import numpy
N,M = list(map(int,input().split()))
arr=numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(arr,axis=0),axis=0))


# ### Function 10: Min and Max

# In[13]:


import numpy
N,M=list(map(int,input().split()))
A=numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A,axis=1)))


# ### Function 11: Mean, var and std

# In[ ]:


import numpy
N,M=list(map(int,input().split()))
A=numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(numpy.std(A,axis=None))


# ### Function 12: Dot and cross

# In[ ]:


import numpy
N=int(input())
A=numpy.array([input().split() for _ in range(N)],int)
B=numpy.array([input().split() for _ in range(N)],int)
print(numpy.dot(A,B))


# ### Function 13: Inner and Outer

# In[15]:


import numpy
A=numpy.array(input().split(),int)
B=numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))


# ### Function 14: Polynomials

# In[16]:


import numpy
a=list(map(float,input().split()))
x=int(input())
print(numpy.polyval(a,x))


# ### Function 15: Linear Algebra

# In[ ]:


import numpy
n=int(input())
A=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(sign=' ')
print(numpy.linalg.det(A))


# In[ ]:




