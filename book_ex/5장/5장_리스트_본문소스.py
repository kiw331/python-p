#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p134.py
ca=[10,11,21]
print(ca)
print(ca[0])
print(ca[1])
print(ca[2])


# In[2]:


#p136.py  # 책 코드에 print(lista) 가 프리트문 중 가장 먼저 실행하는 것으로 수정되어야 함.
lista=[1, "python", 3.9, '프로그래밍']
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# In[3]:


#p138.py
a = [1, 2, 3, 4, 5]
a[2] = 30
print(a)
a[3] = 40
print(a)


# In[4]:


#p139_1.py
listc=[]
print(listc)
listc.append(300)
print(listc)
listc.append("파이썬")
print(listc)
listc.append(3.7)
print(listc)


# In[5]:


#p139_2.py
#listd=[]
#listd[0]=10


# In[6]:


#p140_1.py
listd=[]
listd.append(10)


# In[7]:


#p140_2.py
liste = ['apple', 'banana', 'cherry', 'orange']
print(liste.index('banana'))


# In[8]:


#p141_1.py
na = [5, 6, 1, 9, 4]
for i in range(0, 5, 1):
    print(na[i])


# In[9]:


#p141_2.py
nb = [5, 6, 1, 9, 4]
for nc in nb:
    print(nc)


# In[10]:


#p142_1.py

for nd in [5, 6, 1, 9, 4]:
    print(nd)


# In[11]:


#p142_2.py  #책에 nc => na로 수정해야함
na = [0, 6, 1, 9, 4]
k = len(na)
print(k)


# In[12]:


#p143_1.py #책에 nc => na로 수정해야함
na = [0, 6, 1, 9, 4]
k = len(na)
for i in range(0, k, 1):
    print(na[i])


# In[13]:


#p143_2.py  #책에 변수명 list => nc로 수정해야함
str = 'Hello, World!'
print(len(str))
nc = [1, 2, 3, 4, 5]
print(len(nc))
dict = {'name': 'John', 'age':       25,  'city':'New York'}
print(len(dict))
set = {1, 2, 3, 4, 5}
print(len(set))


# In[14]:


#p143_3.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_without_3 = []

for num in numbers:
    if num % 3 != 0:
        numbers_without_3.append(num)
        
print(numbers_without_3)


# In[15]:


#p144_1.py
a = (1, 2, 3)
print(a)
print(type(a))


# In[16]:


#p145_1.py
a = (1, 2, 3)
print(a[0])
print(a[1])
print(a[2])


# In[17]:


#p145_2.py #책에  range(0, 1, 3) => range(0, 3, 1)로 수정해야함
a = (1, 2, 3)
for sa in range(0, 3, 1):
    print(a[sa])


# In[18]:


#p145_3.py
a = (1, 2, 3)
for sa in a:
    print(sa)


# In[19]:


#p146_2.py
a = (1, 2, 3)
print(a, "a의 데이터형식은", type(a))
b = list(a)
print(b, "b의 데이터형식은", type(b))
b[0] = 7
print(b) 


# In[20]:


#p148.py
dica = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dica)
print("*******************************************************************")
print(dica['애플'])
print(dica['파이썬'])
print(dica['마소'])


# In[21]:


#p149.py
dic = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dic.items())
print(dic.keys())
print(dic.values())


# In[23]:


#p150.py
dicb = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dicb)
print("*******************************************************************")
for sb in dicb:
    print(sb)


# In[24]:


#p151_1.py
dicc = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dicc.keys())
print("*******************************************************************")
for sc in dicc.keys():
    print(sc)


# In[27]:


#p151_2.py
dicf = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dicf.values())
print("*******************************************************************")
for sf in dicf.values():
    print(sf)


# In[28]:


#p152_1.py
dicd = {'애플': 'apple.com','파이썬': 'python.org','마소': 'microsoft.com' }
print(dicd.items())
print("*******************************************************************")
for sd, se in dicf.items():
    print(sd, se)


# In[31]:


#p152_2.py
dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {}

for ka, va in dict1.items():
    dict3[ka] = va
for kb, vb in dict2.items():
    dict3[kb] = vb
print(dict3)


# In[32]:


#p153.py
dica={'이름':'홍길동', '학번':12345, '학점': 4.5}
dica["학과"]="경영학과"
print(dica)


# In[33]:


#p154_1.py
dica={'이름':'홍길동', '학번':12345, '학점': 4.5}
a='학과'
b='경영학과'
dica[a]=b
print(dica)


# In[34]:


#p154_2.py
dica={'이름':'홍길동', '학번':12345, '학점': 4.5}
da=input("입력하고자 하는 요소키를 입력하세요: ")
db=input("입력하고자 하는 요소값을 입력하세요: ")
dica[da]=db
print(dica)


# In[35]:


#p155_1.py
lista=['이름', '학번', '학점']
listb=['홍길동', 12345, 4.5]
dicta={}
dicta[lista[0]]=listb[0]
dicta[lista[1]]=listb[1]
dicta[lista[2]]=listb[2]
print(dicta)


# In[36]:


#p155_2.py
lista=['이름', '학번', '학점']
listb=['홍길동', 12345, 4.5]
dicta={}

for i in range(len(lista)):
    dicta[lista[i]] = listb[i]

print(dicta)


# In[39]:


#p158_1.py # 책에 if 조건문 다음 들여쓰기 안되어 있음=>들여쓰기 수정해야함 
#책에 numbers변수 2번 정의되어 있음 하나 삭제해야함
numbers = [1, 3, 5, 7, 9]

if 7 in numbers:
    print("숫자 7이 리스트에 포함되어 있습니다")
else:
    print("숫자 7이 리스트에 포함되어 있지 않습니다")


# In[38]:


#p158_2.py# 책에 if 조건문 다음 들여쓰기 안되어 있음=>들여쓰기 수정해야함 
#책에 person변수 2번 정의되어 있음 하나 삭제해야함
person = {"name":"john", "age":30, "city":"NewYork"}

if "name" in person:
    print("'name' 키가 딕셔너리에 포함되어 있습니다.")
else:
    print("'name'키가 딕셔너리에 포함되어 있지 않습니다")

