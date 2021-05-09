#!/usr/bin/env python
# coding: utf-8

# ## Task - 5

# ### Function 1: Floating point numbers

# In[1]:


import re
for i in range(int(input())):
    print(bool(re.search(r"^[+-]?\d*\.\d+$",input().strip())))


# ### Function 2: Re.split()

# In[2]:


regex_pattern = r"[,.]"	
import re
print("\n".join(re.split(regex_pattern, input())))


# ### Function 3: Groups()

# In[4]:


import re
m = re.search(r'([A-Za-z0-9])\1+',input())
if m:
    print(m.group(1))
else:
    print(-1)


# ### Function 4: Re.findall() & Re.finditer()

# In[5]:


import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)
if match:
    for i in match:
        print(i)
else:
    print('-1')


# ### Function 5: Re.start() & Re.end()

# In[6]:


import re
S = input()
k = input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    print (m.start(1),m.end(1)-1)
if anymatch == 'No':
    print(-1, -1)


# ### Function 6: Regex substitution 

# In[ ]:


import re

for line in range(int(input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print(string)


# ### Function 7: Validating Roman Numerals

# In[8]:


import re
print(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",input())))


# ### Function 8: Validating phone numbers

# In[10]:


import re
for i in range(int(input())):
    print('YES' if re.search(r"^[789]\d{9}$",input()) else 'NO')
  


# ### Function 9: Validating and Parsing Email Addresses

# In[12]:


import re
from email.utils import *
for i in range(int(input())):
    email = parseaddr(input())
    if bool(re.search(r'^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$', email[1])):
        print(formataddr(email))


# ### Function 10: Hex Color Code

# In[13]:


from __future__ import print_function
import re

css = ""
for i in range(int(input())):
    css+=input()
    css+='\n'

inside_brackets = re.findall(r'\{.*?\}', css, flags=re.DOTALL)
for property in inside_brackets:
    map(lambda i: print(i,sep='\n',end='\n'),(re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', property)))


# ### Function 11: HTML Parser - Part 1

# In[ ]:


from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :',tag)
        for attr in attrs:
                print('->',' > '.join(map(str,attr)))
    def handle_endtag(self, tag):
        print('End   :',tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :',tag)
        for attr in attrs:
                print('->',' > '.join(map(str,attr)))

html = ""
for i in range(int(input())):
    html += input()
                    
                
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ### Function 12: HTML Parser - Part 2

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data:
            print('>>> Single-line Comment')
            print(data)
        elif '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ### Function 13

# In[15]:


from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->"," > ".join(attr))

parser = MyHTMLParser()

html = ""
for i in range(int(input())):
    html += input()
    html += '\n'


parser.feed(html)


# ### Function 14: Validating UID

# In[16]:


import re
for i in range(int(input())):
    N = raw_input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print('Invalid')
            else:
                print('Valid')    
        else:
            print('Invalid')
    else:
        print('Invalid')


# ### Function 15

# In[ ]:


import re
for i in range(int(input())):
    S = raw_input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        print('Invalid' if final_match else 'Valid')
    else:
        print('Invalid')


# ### Function 16

# In[ ]:


import re
P = input()
print(len(re.findall(r'(?=(\d)\d\1)',P)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',P)))


# ### Function 17

# In[ ]:


import re
matrix = []
N,M = map(int,input().split())
for i in range(N):
    matrix.append(list(raw_input()))
print re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ',"".join("".join(decode) for decode in zip(*matrix)))


# In[ ]:




