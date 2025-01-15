#!/usr/bin/env python
# coding: utf-8

# In[3]:


#p259.py
class Cvalue:
    
    def __init__(self):
        self.lista=[]
        
    def add(self, num):
        self.lista.append(num)
        
    def fprint(self):
        print(self.lista)
        
p1=Cvalue()
p1.add(1)
p1.add(2)
p1.add(3)
p1.fprint()
            
        


# In[9]:


#mex1.py    #p260
#이 프로그램을 mex1.py 로 따로 저장해야 한다.
#import 하는 프로그램과 같은 폴더에 저장한다. 
class Cvalue:
    
    def __init__(self):
        self.lista=[]
        
    def add(self, num):
        self.lista.append(num)
        
    def fprint(self):
        print(self.lista)
def plus(a, b):
    c = a + b
    return c
        
p1=Cvalue()
p1.add(1)
p1.add(2)
p1.add(3)
p1.fprint()


# In[8]:


#p262.py
import mex1

p2 = mex1.Cvalue()
p2.add(1)
p2.add(2)
p2.add(3)
p2.fprint()
value = mex1.plus(10, 20)
print(value)


# In[13]:


#mex4.py #p265  #책에 selflista.append(num)-> self.lista.append(num) 수정해야 함. 


class Cvalue:
    
    def __init__(self):
        self.lista=[]
        
    def add(self, num):
        self.lista.append(num)#책에 selflista.append(num)-> self.lista.append(num)
        
    def fprint(self):
        print(self.lista)
def plus(a, b):
    c = a + b
    return c

if __name__ == "__main__":
        
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()


# In[14]:


#p266.py
from mex4 import plus

value = plus(10, 20)
print(value)


# In[15]:


#p270.py
class Cvalue:
    cnum = 0
    def add(self, num):
        self.cnum = self.cnum + num
p1 = Cvalue()
p2 = Cvalue()
p3 = Cvalue()

a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
b=p2.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p2.cnum", p2.cnum)
c=p3.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p3.cnum", p3.cnum)


# In[17]:


#p271.py
class Cvalue:
    cnum = 0
    def add(self, num):
        self.cnum = self.cnum + num
        Cvalue.cnum = Cvalue.cnum + 1
p1 = Cvalue()
p2 = Cvalue()
p3 = Cvalue()

a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
a=p1.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p1.cnum", p1.cnum)
b=p2.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p2.cnum", p2.cnum)
c=p3.add(3)
print("Cvalue.cnum", Cvalue.cnum, "p3.cnum", p3.cnum)


# In[19]:


#ㅔ272,py
'''클래스멤버변수와 인스턴스 멤버변수는
어디에서나 접근 가능한 멤버변수와 함수내에서만 접근가능한 지역변수를
global을 이용 전역변수로 사용하도록 하는 것과 유사한 기능으로 이해를 위해
아래 코드를 실행시켜 보자'''
cnum = 0
def add(num):
    global cnum
    cnum = cnum + num
    print("addcnum", cnum)
add(3)
print("cnum", cnum)
add(3)
print("cnum", cnum)
add(3)
print("cnum", cnum)


# In[ ]:




