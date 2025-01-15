#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p186.py
na=10
nb=11
print("na값은 ", na, "nb 값은 ", nb)
temp=na
na=nb
nb=temp
print("na값은 ", na, "nb 값은 ", nb)


# In[2]:


#p188.py
def funca(pa, pb):
    temp = pa
    pa=pb
    pb=temp
    
na=10
nb=11
print("na값은 ", na, "nb 값은 ", nb)
funca(na, nb)
print("na값은 ", na, "nb 값은 ", nb)


# In[3]:


#p190.py
def funca(na, nb):
    temp = na
    na=nb
    nb=temp
    
na=10
nb=11
print("na값은 ", na, "nb 값은 ", nb)
funca(na, nb)
print("na값은 ", na, "nb 값은 ", nb)


# In[4]:


#p193.py
def funca(na, nb):
    temp = na
    na=nb
    nb=temp
    
na=10
nb=11
print("na값은 ", na, "nb 값은 ", nb)
funca(na, nb)
print("na값은 ", na, "nb 값은 ", nb)


# In[5]:


#p196.py
b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test():
    a = 1
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖의 a 값은", a)
scope_test()
print("scope_test() 함수 호출 후  a 값은", a)


# In[6]:


#p197.py
b = 0
print("b의 값은", b)

b = 1
print("b의 값은", b)

def scope_test():
    global a
    a = 1
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖의 a 값은", a)

scope_test()
print("scope_test() 함수 호출 후  a 값은", a)


# In[7]:


#p198.py
b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test():
    a = a + 3
    print("scope_test() 함수 안의 a 값은", a)

a = 0
print("scope_test() 함수 밖의 a 값은", a)
scope_test()
print("scope_test() 함수 호출 후  a 값은", a)


# In[8]:


#p202.py

def persona(width, height):
    print("함수디폴트값없음, width=", width, "height=", height)
    
def personb(width=4, height=3):
    print("함수디폴트값설정, width=", width, "height=", height)
    
persona(10, 20)
persona()
personb()


# In[9]:


#p204.py

def persona(width, height):
    print("함수디폴트값없음, width=", width, "height=", height)
    
def persona():
    print("매개변수없는 함수")
    
def personb(width=4, height=3):
    print("함수디폴트값설정, width=", width, "height=", height)
    
persona(10, 20)
persona()
personb()


# In[10]:


#p205_1.py

def persona(width=11, height=21):
    print("함수디폴트값설정, width=", width, "height=", height)
    
def personb(width=4, height=3):
    print("함수디폴트값설정, width=", width, "height=", height)
    
persona(10, 20)
persona()
personb()


# In[12]:


def fget(nums = [0]):
    return nums
result1 = fget()
print(result1)
result2 = fget([1, 2, 3])
print(result2)


# In[ ]:




