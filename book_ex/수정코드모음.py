#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p44_45.py #책에서 코드 p45정답제시시a->na, b->nb로 변경해야함
na = 20
nb = 5
result = na - nb
print(na, "-", nb, "=", result, "이다" )
result = na * nb
print(na, "*", nb, "=", result, "이다")
result = na / nb
print(na, "/", nb, "=", result, "이다")


# In[ ]:


#p121_1.py #  책 코드에 i n 띄어쓰기 in 으로 수정해야함
for j in range(1, 6, 1):
    for i in range(1, 10, 1):
        print(j, "*", i, "=", j * i )


# In[ ]:


#p136.py  #  print(lista)가 프린트문 중 가장먼저 실행해야 오른쪽 실행결과가 나옴
lista=[1, "python", 3.9, '프로그래밍']
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# In[ ]:


#p142_2.py  #리스트명 책에 nc를 na로 수정
na = [0, 6, 1, 9, 4]
k = len(na)
print(k)


# In[ ]:


#p143_1.py #리스트명 책에 nc를 na로 수정
na = [0, 6, 1, 9, 4]
k = len(na)
for i in range(0, k, 1):
    print(na[i])


# In[ ]:


#p145_2.py #책에  range(0, 1, 3)을 range(0, 3, 1)로 수정
a = (1, 2, 3)
for sa in range(0, 3, 1):
    print(a[sa])


# In[ ]:


#p143_2.py #리스트명  책에 list fmf nc로 수정
#한줄코드 2줄로 표시시 역슬래시(\)사용
str = 'Hello, World!'
print(len(str))
nc = [1, 2, 3, 4, 5]
print(len(nc))
dict = {'name': 'John', 'age':       25,  'city':'New York'}
print(len(dict))
set = {1, 2, 3, 4, 5}
print(len(set))


# In[ ]:


#p158_1.py # 책에 if 조건문 다음 들여쓰기 안되어 있음
numbers = [1, 3, 5, 7, 9]

if 7 in numbers:
    print("숫자 7이 리스트에 포함되어 있습니다")
else:
    print("숫자 7이 리스트에 포함되어 있지 않습니다")


# In[ ]:


#p158_2.py# 책에 if 조건문 다음 들여쓰기 안되어 있음
person = {"name":"john", "age":30, "city":"NewYork"}

if "name" in person:
    print("'name' 키가 딕셔너리에 포함되어 있습니다.")
else:
    print("'name'키가 딕셔너리에 포함되어 있지 않습니다")


# In[ ]:


#p171.py#함수 호출시 함수명 책에fadd->funca로 변경해야함
#print문 책에 a->na, b->nb로 

def funca(pa, pb):
    nc = pa + pb

na = 10
nb = 11
    
funca(na, nb)
print(na, "+", nb, "=", nc)


# In[ ]:


#p172.py # 책에 a->na, b->nb
def funca(pa, pb):
    nc = pa + pb
    return nc

na = 10
nb = 11
    
nd=funca(na, nb)
print(na, "+", nb, "=", nd)


# In[ ]:


#p227_2[step 5].py # 중간에 명령문이 2번 들여쓰기 안된상태로 쓰임
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


# In[ ]:


#mex4.py #p265  #책에 selflista.append(num)-> self.lista.append(num)

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

if __name__ == "__namin__":
        
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()


# In[ ]:


#p345_2.py #책에 numa[-1]->muna[-1]로 교체해야함
muna = "python"
print(muna[0])
print(muna[-1])


# In[ ]:


#p289_1.py #코드 자체를 다 교체해야함 # 오른쪽 그림도 교체해야함
import tkinter
oroot = tkinter.Tk()
oroot.geometry("200x100")
obutton1 = tkinter.Button(oroot, text="PUSH1")
obutton2 = tkinter.Button(oroot, text="PUSH2")
obutton3 = tkinter.Button(oroot, text="PUSH3")
obutton1.grid(row=1, column=0)
obutton2.grid(row=1, column=1)
obutton3.grid(row=0, column=4)
oroot.mainloop()

