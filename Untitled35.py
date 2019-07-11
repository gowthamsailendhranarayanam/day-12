#!/usr/bin/env python
# coding: utf-8

# d1 = {"Name":"Gitam","EmailId":"gitam@gmail.com","Address":"Hyderabad"}
# print(d1)

# In[2]:


def secondlarge(li):
   li.sort()
   return li[-2]
def genericlarge(li,n):
   li.sort()
   return li[-n]
li = [1,19,6,2,8,18,3]
genericlarge(li,4


# In[3]:


# function for conversation - number to list
# output --- number
# output -- list
# test cases :-
# 14569 -- [1,4,5,6,9]
# 1990 -- [ 1,9,9,0]
 
def numberlistconversion(n):
li=[]
while n!=0:
  r=n%10
  li.append(r)
  n=n//10
li.reverse()
return li
numberlistconversion(14569)#[1,4,5,6,9]


# In[4]:


def countcharoccurances(s,c):
   cnt = 0
   for ch in s:
       if ch == c:
           cnt += 1
   return cnt
countcharoccurances("python programming", 'm')


# #function to represent the bubble sort
# def bubbleSort(li):
#    for i in range(len(li)-1):
#        for j in range(len(li)-1):
#            if li[j]>li[j+1]:
#                li[j],li[j+1]=li[j+1],li[j]
#    return li
# li=[19,1,25,6,18,3]
# bubbleSort(li)

# ##tupules
# .t1 parenthesis() li square brackets[]
# . difference between list and tuples
# . lists are mutable-can be changed

# contact application
# list all co9mmands
# name 1:phone1
# name2:phone2
# modifiy the  contact
# remove the contact
# import the contact

# In[9]:


#add contacts
contacts ={}
def addContact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact is details are added")
    else:
            print("contact detail;s are already exists")
            return
addContact('rogi','952121632')
addContact('rogi','952121632')
addContact('rogio','952121532')


# In[11]:


lst2=[]
lst=[1,3,9,27,81]
y=0
for i in lst:
    lst2.append(i+y)
    y=i
print(lst2)


# In[12]:


lst=[1,3,9,27,81]
for i in lst:
    if i%2==0:
        print(i, end="")


# In[13]:


def reverseFib(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    for i in range(2, n):  
        a[i] = a[i - 2] + a[i - 1]
    for i in range(n - 1, -1 , -1):  
        print(a[i],end=" ")
        
n = 5
reverseFib(n)


# In[15]:


n=int(input("Enter number:"))
m = str(n)
count=0
while(n>0):
   count=count+1
   n=n//10
i=0
for i in range(count):
   print('*'*int(m[i]))


# In[16]:


def countcharoccurances(s,c):
   cnt = 0
   for ch in s:
       if ch == c:
           cnt += 1
   return cnt
countcharoccurances("python programming", 'm')


# In[ ]:


### packages and modules

**packages:**
    -> a collection of modules (single python file. py) and subpackages
    module
      ->a single python file containing set functions
   packages --> sub packages --> modules ---> function ---> statements


# In[18]:


import math
math.floor(123.45)


# In[20]:


from math import factorial as fact
fact(5)


# In[21]:


from math import gcd as fact
gcd(10,15)


# In[ ]:


### standard libraries
- file i/o
- regular expressions
- date  time
-math(numerical and mathematical


# write, read,analysis,-data science and analysis
# ###file handling in python
# - file:- document containing information resides on the permenant storage 
# different types of files :- txt,doc,pdf,csv,and etc
# input -- keyboard
# output file
# ### modes of the file i/o
# -'w'-- this is used to file writing
#      -- if the file is not present first it creates the file and write to the file
#      

# In[3]:


# function to create a file or write a file
def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line' % i)
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[ ]:





# In[ ]:





# In[4]:


cat file1.txt


# In[5]:


ls


# In[1]:


def appendData(filename):
    f = open(filename,'a')
    f.write("new Line 1 \n" % i)
    f.write("new Line 2 \n" % i)
    print("file created and succesfully data written")
    return
appendData("file2.txt")
    


# In[19]:


def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line \n' % i)
    print("file is created and data has written")
    return
createfile('file2.txt')


# In[20]:


# function  to read a file
def readFileData(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        X = f.read()
        print(X)
    f.close()
    return
readFileData('file2.txt')


# In[ ]:


#data analysis
def worfcount(filename,word):
    with open(filename,'r') as f:
        if f.mode = 'r':
            x=f.read()
            li = x.split()
        cnt = li.count(word)  
    return
filename = input('enter the file name : ')
word = input('enter the word :')
wordcount()


# In[22]:


def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x =f.read()
            li = list(x)
    return len(li)
filename = input('enter the filename : ')
charcount(filename)


# In[23]:


fname = input("Enter file name: ") num_lines = 0 with open(fname, 'r') as f: for line in f: num_lines += 1 print("Number of lines:") print(num_lines)
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
  for line in f:
      num_lines += 1
print("Number of lines:")
print(num_lines)


# In[24]:


def countOfLines(filename):
   with open(filename,'r') as f:
       if f.mode=='r':
           x=f.read()
           li=x.split("\n")
   return len(li)
filename=input('Enter the filename : ')
countOfLines(filename)


# In[26]:


# Function to print the Upper and Lower characters
def caseCount(filename):
   cntUpper=0
   cntLower=0
   with open(filename,'r') as f:
       if f.mode == 'r':
           x=f.read()
           li=list(x)
   for i in li:
       if i.isupper():
           cntUpper += 1 #cntUpper = cntUpper + 1
       elif i.islower():
           cntLower += 1 #cntLower + 1
           output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
   return output
filename = input('Enter the filename : ')
caseCount(filename)


# In[27]:


#os package it contains the certain method which works with os
ls


# In[28]:


ls


# In[30]:


cd Desktop/pythonprog/Git


# In[31]:


li = os.scandir('Git/')
for i in li:
    print(i)


# In[33]:


# Function to print the Upper and Lower characters
def caseCount(filename):
   cntUpper=0
   cntLower=0
   with open(filename,'r') as f:
       if f.mode == 'r':
           x=f.read()
           li=list(x)
   for i in li:
       if i.isupper():
           cntUpper += 1 #cntUpper = cntUpper + 1
       elif i.islower():
           cntLower += 1 #cntLower + 1
            output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
   return output
filename = input('Enter the filename : ')
caseCount(filename)


# In[34]:


ls


# In[ ]:




