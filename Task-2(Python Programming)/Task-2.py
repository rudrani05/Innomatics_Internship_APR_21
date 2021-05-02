#!/usr/bin/env python
# coding: utf-8

# ## Task 2

# ### Problem 1: List Comprehension

# In[8]:


x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([[a,b,c] for a in range(0,1+x) for b in range(0,1+y) for c in range(0,1+z) if a+b+c!=n])


# ### Problem 2: Find the runner-up score

# In[15]:


n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
li=sorted(set(arr))
li.remove(max(li))
print('Runner-up score:{}'.format(max(li)))


# ### Problem 3: Nested Lists

# In[25]:


l=[]
sc_n=[]
scores=set()
n=int(input())
for i in range(n):
    names=input()
    score=float(input())
    l.append([names,score])
    scores.add(score)
second_low=sorted(scores)[1]
for name,score in l:
    if score==second_low:
        sc_n.append(name)
for name in sorted(sc_n):
    print(name,end='\n')


# ### Problem 4: Finding the percentage

# In[66]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key, value in student_marks.items():
        if query_name == key:
            sum = 0
            count = 0
            for i in value:
                sum += i
                count += 1
            average = sum/count
            print("{:.2f}".format(average))


# ### Problem 5: Lists

# In[44]:


N=int(input())
l=[]
for i in range(N):
    s=input().strip().split(" ")
    if s[0]=='insert':
        l.insert(int(s[1]),int(s[2]))
    elif s[0]=='append':
        l.append(int(s[1]))
    elif s[0]=='remove':
        l.remove(int(s[1]))
    elif s[0]=='pop':
        l.pop()
    elif s[0]=='sort':
        l.sort()
    elif s[0]=='reverse':
        l.reverse()
    elif s[0]=='print':
        print(l)


# ### Problem 6: Tuples

# In[47]:


n = int(input())
ints = input().split()
t = tuple(int(i) for i in ints)
print(hash(t))


# ### Function 7: Sets

# In[48]:


def average(array):
    return (sum(set(arr)))/len(set(arr))   
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# ### Function 8: No idea

# In[49]:


n,m=input().split()
arr=input().split()

A=set(input().split())
B=set(input().split())
sum=0
for i in arr:
    if i in A:
        sum+=1
    elif i in B:
        sum+=-1
print(sum)            


# ### Function 9: Symmetric difference

# In[50]:


M=int(input())
m=input()
N=int(input())
n=input()

a=list(map(int,m.split()))
b=list(map(int,n.split()))

x=set(a)
y=set(b)

c=x.difference(y)
d=y.difference(x)

s=c.union(d)
e=list(sorted(s))

for i in range(len(e)):
    print(e[i])


# ### Function 10: set.add()

# In[51]:


N=int(input())
n=set()
for i in range(N):
    n.add(input())
print(len(n))    


# ### Function 11: Set .discard(), .remove() & .pop()

# In[52]:


n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    string=input().split()
    if string[0]== 'pop':
        s.pop()
    elif string[0]=='remove':
        s.remove(int(string[1]))
    elif string[0]=='discard':
        s.discard(int(string[1]))
print(sum(s))               


# ### Function 12: Set .union()

# In[53]:


N=int(input())
n=set(input().split())
M=int(input())
m=set(input().split())

print(len(n.union(m)))


# ### Function 13: Set .intersection()

# In[54]:


N=int(input())
n=set(input().split())
M=int(input())
m=set(input().split())
print(len(n.intersection(m)))


# ### Function 14: Set .difference() Operation

# In[55]:


N=int(input())
n=set(input().split())
M=int(input())
m=set(input().split())
print(len(n.difference(m)))


# ### Function 15: Set .symmetric_difference() Operation

# In[56]:


N=int(input())
n=set(input().split())
M=int(input())
m=set(input().split())
print(len(n.symmetric_difference(m)))


# ### Function 16: Set Mutations

# In[57]:


n=int(input())
A=set(map(int,input().split()))
N=int(input())

for _ in range(N):
    c,_=input().split()
    S=set(map(int,input().split()))
    if c=='intersection_update':
        A.intersection_update(S)
    elif c=='update':
        A.update(S)
    elif c=='symmetric_difference_update':
        A.symmetric_difference_update(S)
    elif c=='difference_update':
        A.difference_update(S)
print(sum(A))                   


# ### Function 17: The Captain's Room 

# In[58]:


K=int(input())
a=input().split()
s1=set()
s2=set()

for i in a:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print(s3.pop())            


# ### Function 18: Check Subset

# In[61]:


for _ in range(int(input())):
    x,a,y,b=input(),set(input().split()),input(),set(input().split())
    print(a.issubset(b))


# ### Function 19: Check Strict Superset

# In[60]:


a=set(input().split())
counter,n=0,int(input())
for i in range(n):
    b=set(input().split())
    if a.issuperset(b):
        counter+=1
print(counter==n)        

