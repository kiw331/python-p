#!/usr/bin/env python
# coding: utf-8

# In[3]:


#p207_1.py
na=10
nb=11
print("na =", na, "nb =", nb)
temp=na
na=nb
nb=temp
print("na =", na, "nb =", nb)


# In[4]:


#p207_2.py
ca=[10,11]
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
temp=ca[0]
ca[0]=ca[1]
ca[1]=temp
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])


# In[5]:


#p208.py
ca=[10,11]
print("ca[0]=", ca[0], "ca[1]=", ca[1])
temp=ca[0]
ca[0]=ca[1]
ca[1]=temp
print("ca[0]=", ca[0], "ca[1]=", ca[1])


# In[10]:


#p209.py
def funca(na, nb):
    temp=na
    na=nb
    nb=temp
   

ca=[10,11]
na=ca[0]
nb=ca[1]
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])
funca(ca[0], ca[1])
print("ca[0]의 값은", ca[0], "ca[1]의 값은", ca[1])


# In[11]:


#p211.py
ca=[10, 11]
cb=ca
print("리스트ca값은", ca)
print("리스트cb값은", cb)


# In[12]:


#p212.py
ca=[10, 11]
cb=ca
print("리스트ca값은", ca)
print("리스트cb값은", cb)
temp=cb[0]
cb[0]=cb[1]
cb[1]=temp
print("리스트ca값은", ca)
print("리스트cb값은", cb)
print("ca[0]=", ca[0], "ca[1]=", ca[1])
print("cb[0]=", cb[0], "cb[1]=", cb[1])


# In[14]:


#p213.py
def funca(cb):
    temp=cb[0]
    cb[0]=cb[1]
    cb[1]=temp
    
ca=[10, 11]

print("ca[0] 값은", ca[0], "ca[1] 값은", ca[1])
funca(ca)
print("ca[0] 값은", ca[0], "ca[1] 값은", ca[1])


# In[15]:


#p214.py
a=[10, 11, 12, 13]
print("리스트 a값", a)
b=a
print("리스트 b값",b)


# In[16]:


#p214.py
a=[10,11,12,13]
print("리스트 a값", a)
a[1]=21
print("리스트 a값",a)
b=a
print("리스트 b값",b)
b=[30, 31, 32, 33]
print("리스트 b값",b)


# In[17]:


#p216_2.py
def fk(cb):
    total = 0
    for sb in range(0, 3, 1):
        total = total + cb[sb]
    cb[2] = total
    return cb

ca = [10, 20, 30]
print(ca)
cd = fk(ca)
print(ca)
print(cd)


# In[18]:


#p222.py
#선택정렬_완성코드
ca=[21,10,11,15,13]
mina=ca[0]
minix=0
for sb in range(1, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb
temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp
print(ca)
mina=ca[1]
minix=1
for sb in range(2, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb
temp = ca[1]
ca[1] = ca[minix]
ca[minix] = temp
print(ca)
mina=ca[2]
minix=2
for sb in range(3, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb
temp = ca[2]
ca[2] = ca[minix]
ca[minix] = temp
print(ca)
mina=ca[3]
minix=3
for sb in range(4, 5, 1):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb
temp = ca[3]
ca[3] = ca[minix]
ca[minix] = temp
print(ca)


# In[19]:


#p226_1.py
su=[5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    max=a
    if max < b:
        max=b
    if max < c:
        max=c
    if max < d:
        max=d
    if max < e:
        max = e
    return max
a=su[0]
b=su[1]
c=su[2]
d=su[3]
e=su[4]    

max=fmax(su[0],su[1],su[2],su[3],su[4])

print("최대값 max는", max)


# In[ ]:


#p226_2.py
su=[5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu=[a, b, c, d, e]
    max=fu[0]
    if max < fu[1]:
        maxfu[1]
    if max < fu[2]:
        max=fu[2]
    if max < fu[3]:
        max=fu[3]
    if max < fu[4]:
        max = fu[4]
    return max

a=su[0]
b=su[1]
c=su[2]
d=su[3]
e=su[4]
max=fmax(su[0],su[1],su[2],su[3],su[4])
print("최대값 max는", max)


# In[20]:


#p227_1[ste[3].py
su=[5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu=[a, b, c, d, e]
    max=fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max = fu[i]
    return max

a=su[0]
b=su[1]
c=su[2]
d=su[3]
e=su[4]
max=fmax(su[0],su[1],su[2],su[3],su[4])
print("최대값 max는", max)


# In[21]:


#p227_1[step4].py
su=[5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu=[a, b, c, d, e]
    max=fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

a=su[0]
b=su[1]
c=su[2]
d=su[3]
e=su[4]
max=fmax(su[0],su[1],su[2],su[3],su[4])
print("최대값 max는", max)


# In[22]:


#p227_2[step 5].py
# 중간에 같은 명령문이 2번 들여쓰기 안된 상태로 쓰임 삭제해야함
su=[5, 4, 7, 10, 6]

def fmax(a, b, c, d, e):
    fu=[]
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max=fu[0]
    for sfu in fu:
        if max < sfu:
            max=sfu
    return max
       
max=fmax(su[0],su[1],su[2],su[3],su[4])
print("최대값 max는", max)


# In[23]:


#p227_3[step6].py
su=[5, 4, 7, 10, 6]

def fmax(fu):
   
    max=fu[0]
    for sfu in fu:
        if max < sfu:
            max=sfu
    return max
       
max=fmax(su)
print("최대값 max는", max)


# In[24]:


#p228_1.py
su=[5, 4, 7, 10, 6]
def fmax(fu):       
    max=fu[0]
    for i in range(1, 5, 1):
        if max < fu[i]:
            max=fu[i]
    return max
fu = su       
max=fmax(su)
print("최대값 max는", max)


# In[25]:


#p229.py
a={1:"월", "tue":"화", "wed":"수"}
print(a)
x=a
print(x)
x[1]="일"
print(x)
print(a)


# In[26]:


#p230.py
def fch(x):
    x[1] ="일"
a={1:"월", "tue":"화", "wed":"수"}
print(a)
fch(a)
print(a)


# In[ ]:




