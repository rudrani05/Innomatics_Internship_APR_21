#!/usr/bin/env python
# coding: utf-8

# ## Task-8

# ### 1.Binomial Distribution I

# In[1]:


import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += bi_dist(i, n, p)   
print("%.3f" %b)


# ### 2. Binomial Distribution II

# In[3]:


def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))


# ### 3. Normal Distribution I

# In[4]:


import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))


# ### 4. Normal Distribution II

# In[5]:


import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))


# ### 5. The Central Limit Theorem I

# In[ ]:


import math

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))


# ### 6. The Central Limit Theorem II

# In[ ]:


import math
x = 250
n = 100
sampling_mean = 2.4
sampling_stdev = 2.0
stdev = sampling_stdev * math.sqrt(n)

cdf = 0.5 * (1 + math.erf((x - sampling_mean * n) / (stdev * math.sqrt(2))))

print(round(cdf,4))


# ### 7. The Central Limit Theorem III

# In[ ]:


samples = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float (input())

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))


# ### 8. Pearson Correlation Coefficient I

# In[ ]:


#input
N = int(raw_input())
X = list(map(float,raw_input().strip().split()))
Y = list(map(float,raw_input().strip().split()))

#Pearson Correlation Coefficent
print(round(sum([(X[i] - sum(X) / N) * (Y[i] -sum(Y) / N) for i in range(N)]) / (N * (sum([(i - (sum(X) / N))**2 for i in X]) / N)**0.5 * (sum([(i - (sum(Y) / N))**2 for i in Y]) / N)**0.5),3))


# ### 9. Least Square Regression Line

# In[ ]:


n = 5
xy = [map(int, input().split()) for _ in range(n)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
print('{:.3f}'.format(a + b * 80))


# ### 10. Multiple Linear Regression

# In[ ]:


#import data
import numpy as np
m,n = [int(i) for i in input().strip().split(' ')]
X = []
Y = []
for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
q = int(input().strip())
X_new = []
for x in range(q):
    X_new.append(input().strip().split(' '))
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

#center
X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

#calculate beta
beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

#predict
X_new_R = X_new-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(Y)

#print
for i in Y_new:
    print(round(float(i),2))


# In[ ]:




