#!/usr/bin/env python
# coding: utf-8

# In[2]:


#p334.py
while True:
    count = input("수량을 입력하세요")
    try:
        count = int(count)
        break
    except:
        print("잘못된 입력입니다")


# In[3]:


#p334_1.py
while True:
    count = input("수량을 입력하세요")
    try:
        count = int(count)
        break
    except ValueError:
        print("잘못된 입력입니다")


# In[6]:


#p334_2.py
while True:
    count = input("수량을 입력하세요")
    if count.isdigit():
        count = int(count)
        break
    else:
        print("잘못된 입력입니다")


# In[7]:


#p336.py
dicta={"월요일":"monday", "화요일":"tuesday", "수요일":"wednesday", "목요일":"thursday", "금요일":"friday", "토요일":"saturday", "일요일":"sunday"}
print("월요일 부터 일요일 중 영어로 번역하고 싶은 요일을 입력하세요")
yoil=input()
print(dicta[yoil])


# In[8]:


#p337.py
dicta={"월요일":"monday", "화요일":"tuesday", "수요일":"wednesday", "목요일":"thursday", "금요일":"friday", "토요일":"saturday", "일요일":"sunday"}
print("월요일 부터 일요일 중 영어로 번역하고 싶은 요일을 입력하세요")
yoil=input()
try:
    print(dicta[yoil])
except KeyError:
    print("요일을 잘못 입력했어요")


# In[10]:


#p338.py
na = 11
nb = 0
if nb!= 0:
    nc = na/nb
else:
    nc = "분모가 0으로 나눌 수 없습니다."
    
print(nc)


# In[12]:


#p338.py
try:
    print(11/0)
except ZeroDivisionError:
    print("0인 분보가 분자를 나눌 수 없습니다")


# In[13]:


#p340py
print("분자값을 입력하세요")
ra = int(input())
print("분모값을 입력하세요")
rb = int(input())

if rb!= 0:
    rc = ra/rb
else:
    rc = "분모가 0으로 나눌 수 없습니다."
    
print(rc)


# In[14]:


#p341_1.py
print("분자값을 입력하세요")
ra = int(input())
print("분모값을 입력하세요")
rb = int(input())

try:
    rc = ra/rb
except ZeroDivisionError:
    rc = "분모가 0으로 나눌 수 없습니다."
    
print(rc)


# In[16]:


#p341_2.py
print("분자값을 입력하세요")
ra = int(input())
print("분모값을 입력하세요")
rb = int(input())

try:
    rc = ra/rb
except ZeroDivisionError:
    rc = "분모가 0으로 나눌 수 없습니다."
    
else:
    print(rc)


# In[18]:


#p342_1.py
muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))
muna[0]='k'


# In[20]:


#p342_2.py
munb = ["python"]
print(munb[0])
print(type(munb))


# In[22]:


#p342_3.py
munc = ["p","y","t","h","o","n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0]='k'
print(munc)


# In[23]:


#p343_1.py
munc = ["p","y","t","h","o","n"]
for i in range(0, 6,1):
    print(munc[i])
    


# In[24]:


#p343_2.py
munc = ["p","y","t","h","o","n"]
length = len(munc)
print(length)
for i in range(0, length,1):
    print(munc[i])


# In[25]:


#p343_3.py
munc = ["p","y","t","h","o","n"]
for i in munc:
    print(i)


# In[27]:


#p345_1.py
ma = "ChatGPT" + "를 활용한  python"
print(ma)


# In[28]:


#p345_2.py  #책에 numa[-1]->muna[-1]로 수정해야함
muna = "python"
print(muna[0])
print(muna[-1])


# In[29]:


#p346.py
muna = "python"
print(muna[2:-1])
print(muna[1:4])
print(muna[:])


# In[30]:


#p347.py
name = "John"
age = 30
print(f"My name is {name} and I'm {age} years old")


# In[31]:


#p348.py
pi = 3.141592
print(f"Pi is aprrosimately {pi:.2f}")


# In[32]:


#p349.py
my_string = "Python is a popular programming language"
split_list =my_string.split()
print(split_list)


# In[33]:


#p350.py
my_string = "Python is awesome!"
stripped_string = my_string.strip()
print(stripped_string)


# In[34]:


#p351.py
my_list = {"apple", "banana", "cherry"}
joined_string = "-".join(my_list)
print(joined_string)


# In[36]:


#p352.py
my_string = 'Hello, world'
replaced_string = my_string.replace("world", "Python")
print(replaced_string)


# In[38]:


#p353.py
square = lambda x : x **2
print(square(3))


# In[39]:


#p354.py
def square(x):
    return x **2

numbers = [1,2,3,4,5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))


# In[42]:


#p355.py
numbers = [1,2,3,4,5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))


# In[ ]:




