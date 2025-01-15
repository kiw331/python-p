#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p168_1.py
def fhello():
    print("매개변수 없는 함수 호출하기")
    
fhello()


# In[3]:


#p168_2.py
def fweather():
    dica = {"아침":5, "점심":10, "저녁":7}
    for a, b in dica.items():
        print(a, "온도는", b, "도이다.")
fweather()


# In[4]:


#p169_1.py
na = 10
nb = 11
nc = na + nb
print(na, "+", nb, "=", nc)


# In[5]:


#p169_2.py
def funca(na, nb):
    nc = na + nb
    print(na, "+", nb, "=", nc)
    
funca(10, 20)


# In[8]:


#p171.py #책에 fadd(na, nb) => funca(na, nb)로 수정해야함
#print문 책에 a->na, b->nb로 수정해야함
#jupyter notebook 이나 코랩 같이 연속적으로 코딩하는 에디터를 쓰는 경우 윗 줄에 nc값이 있다면 정상적으로 실행됨
#그 이유는 위에 있는 코드 중 nc 변수가 있으면 그 변수를 사용해서 실행된 결과임
#이 코드만 따로 코딩해서 결과를 확인해야함
def funca(pa, pb):
    nc = pa + pb

na = 10
nb = 11
    
funca(na, nb)
print(na, "+", nb, "=", nc)


# In[9]:


#p172.py #p172.py # 책에 a->na, b->nb
def funca(pa, pb):
    nc = pa + pb
    return nc

na = 10
nb = 11
    
nd=funca(na, nb)
print(na, "+", nb, "=", nd)


# In[11]:


#p173.py
a=10
b=20

def fadd(a, b):
    nc=a+b
    return nc
    
a=a
b=b

nc=fadd(a,b)
print(a,"+",b,"=", nc)


# In[12]:


#174.py
def freturn(a, b, c, d):
    dica = {a:b, c:d}
    return dica

a = "이름"
b = "이나겸"
c = "학점"
d = 4.3

dicb = freturn(a, b, c, d)
print(dicb)
print(type(dicb))


# In[13]:


#0175.py
myabs(10)

def myabs(arg):
    if(arg < 0):
        result =  arg * -1
    else:
        result = arg 
    return result


# In[14]:


#p176_1.py


def fabs(arg):
    if(arg < 0):
        result =  arg * -1
    else:
        result = arg 
    return result

fabs(10)
    


# In[15]:


#p176_2.py


def fabs(arg):
    if(arg < 0):
        result =  arg * -1
    else:
        result = arg 
    return result

na = fabs(10)
print(na)


# In[16]:


#p177.py

def funca():
    print("funca 함수 호출")
    
def funcb():
    funca()
    print("funcb 함수 호출")

def funcc():
    funcb()
    print("funcc 함수 호출")
    
funcc()


# In[17]:


#ㅔ178.py
def fadd(pa, pb):
    pc = pa + pb
    return pc

na = 10
nb = 20
nc = fadd(na, nb)
print(na, "+", nb, "결괏값은", nc, "이다")


# In[19]:


#p180.py
def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
    
stra = fplusminus(0)
print(stra)


# In[20]:


def finput(pa):
    pb = str(pa)
    return pb

na = 10
print(type(na))
nb = finput(na)
print(nb)
print(type(nb))
nc = int(nb)
print(type(nc))


# In[ ]:




