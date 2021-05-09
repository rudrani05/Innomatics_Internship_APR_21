#!/usr/bin/env python
# coding: utf-8

# ## Task 3

# ### Problem 1: Text Alignment

# In[69]:


thickness = int(raw_input())  # This must me an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) / 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
          (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
print(cmath.polar(num)[1])


# ### Problem 2: sWAP cASE

# In[91]:


def swap_case(s):
    return "".join([i.lower() if i.isupper() else i.upper() for i in s])
if __name__=='__main__':
    s=input()
    result=swap_case(s)
    print(result)


# ### Problem 3: String split and join

# In[96]:


def split_and_join(line):
    line=line.split(" ")
    line='-'.join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ### Problem 4: What's your name

# In[1]:


def print_full_name(first, last):
    print('Hello '+first+' '+ last+'! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ### Problem 5: Mutations

# In[2]:


def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# ### Problem 6: Find a String

# In[3]:


def count_substring(string, sub_string):
    ctr=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            ctr+=1
    return ctr

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# ### Function 7: String Validators

# In[4]:


s = input()
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))


# ### Function 8: Text Wrap

# In[6]:


import textwrap
def wrap(string,max_length):
    return "\n".join(textwrap.wrap(string,max_length))
if __name__=='__main__':
    string,max_length=input(),int(input())
    result=wrap(string,max_length)
    print(result)


# ### Function 9: Designer Door Mat

# In[7]:


N,M=map(int,input().split(" "))
for i in range(N):
    p=".|."
    if i < (N-1)/2:
        print((p*(2*i+1)).center(M,'-'))
    elif i==(N-1)/2:
        print("WELCOME".center(M,"-"))
    else:
        print((p*(2*(N-1-i)+1)).center(M,"-"))        


# ### Function 10: String formatting

# In[8]:


def print_formatted(number):
    w=len(bin(n)[2:])
    for i in range(1,n+1):
        print(str(i).rjust(w),oct(i)[2:].rjust(w),hex(i)[2:].upper().rjust(w),bin(i)[2:].rjust(w))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# ### Function 11: Alphabet Rangoli

# In[19]:


n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))


# ### Function 12: Capitalize

# In[ ]:


def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ### Function 13: 

# In[ ]:


S = input().strip()
S_length = len(S)
player1, player2 = 0,0

for i in xrange(S_length):
    if S[i] in "AEIOU":
        player1 += S_length - i
    else:
        player2 += S_length - i        
        
if player1 > player2:
    print("Kevin", player1)
elif player1 < player2:
    print("Stuart", player2)
else:
    print("Draw")


# ### Function 14

# In[ ]:


s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    t = s[index * k : (index + 1) * k]
    u = ""
    for c in t:
        if c not in u:
            u += c
    print(u)

