#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#mex4.py
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

if __name__ == "__namin__":
        
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()

