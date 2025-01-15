#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p236.py
class Cexm:
    def fsam(self):
        print("멤버함수(메소드)")

ca = Cexm()
ca.fsam()


# In[2]:


#p237.py
class Cexm:
    def fsam(self):
        print("멤버함수(메소드)")
    def fsbm(self, pa):
        self.x = pa
        print("멤버변수 x 는", self.x)

ca = Cexm()
ca.fsam()
ca.fsbm(10)


# In[3]:


#p239.py
class Cexm:
    def fsam(self):
        print("멤버함수(메소드)")
    def __init__(self, pa):
        self.x = pa
        print("멤버변수 x 는", self.x)

ca = Cexm(10)
ca.fsam()


# In[4]:


#p240.py
class Cexm:
    def fssam():
         print("멤버함수가 아니다")
    def fsam(self):
         print("멤버 함수(메소드)")
    def __init__(self, pa, pb): #------------> ①
          self.x = pa
          y = pb
          print("멤버 변수 x 는", self.x) #-> ③
          print("변수 y 는", y) #-> ③

ca = Cexm(10, 20)# --------------------------> ②
ca.fsam()


# In[6]:


#p243_1.py
stra = "abc"
print(stra)


# In[5]:


#p243_2.py
strb=str("abc")
print(strb)
strc=strb.capitalize()
print(strc)


# In[7]:


#p245_1.py
class Cexm:
    def fsam(self):
        print("클래스만들기")
    
    def fadder(self, a,b ):
        self.result = a + b
        return self.result
cal1 = Cexm()
cal1.fsam()
c=cal1.fadder(9,5)
print("메소드 fadder(9,5)호출 결과값은", c,"이다")


# In[9]:


#p245_2.py
class Calculator:
    def setinit(self):
        self.result = 0
    
    def adder(self, num):
        self.result = self.result + num
        return self.result
cal1 = Calculator()
cal1.setinit()
cal2 = Calculator()
cal2.setinit()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


# In[11]:


#p246.py
class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result = self.result + num
        return self.result
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


# In[12]:


#p247.py
class Car:
    def __init__(self, pnum, pspeed):
        self.num = pnum
        self.speed = pspeed        
        
new_car = Car(2023, 90)
print("차량번호", new_car.num)
print("속도는", new_car.speed)


# In[13]:


#p248.pyhttp://localhost:8888/notebooks/Dropbox/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B3%BC%ED%86%B5%EA%B3%84(%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BCR)/%EC%9D%B4%EB%82%98%EA%B2%B8%EC%B1%85%EC%98%88%EC%A0%9C%EB%93%A4_%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9B%8C%ED%81%AC%EB%B6%81_%EC%B5%9C%EC%A2%85%EA%B2%80%EC%88%98%EC%9A%A9/9%EC%9E%A5_%ED%81%B4%EB%9E%98%EC%8A%A4(1)_%EB%B3%B8%EB%AC%B8%EC%86%8C%EC%8A%A4.ipynb#
class Car:
    def __init__(self, pnum, pspeed):
        self.num = pnum
        self.speed = pspeed
    def fprint(self):
        print("차량번호", self.num)
        print("속도는", self.speed)        
        
new_car = Car(2023, 90)
new_car.fprint()


# In[ ]:




