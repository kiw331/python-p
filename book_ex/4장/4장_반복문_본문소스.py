#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p95.py
for sb in (1,2,3):
    print(sb)


# In[2]:


#p96_1.py
for sb in range(1, 4, 1):
    print(sb)


# In[3]:


#p98_2.py
for sb in range(0, 11, 1):
    print(sb)


# In[4]:


#p97_1.py
for sb in range(0, 11, 1):
    print(sb, end=" ")


# In[5]:


#p97_2.py
for sb in range(0, 11, 2):
    print(sb, end=" ")


# In[6]:


#p98_1.py
for sb in range(1, 11, 1):
    if sb%2==0:
        stra="짝수이다"
    else:
        stra="홀수이다"
    print(sb,"는",stra )


# In[7]:


#p99.py
for sb in range(1, 11, 1):
    if sb%2==0:
        continue
        stra="짝수이다"
    else:
        stra="홀수이다"
    print(sb,"는",stra )


# In[9]:


#p100.py
na=int(input("멍추려는 정수값을 입력하세요"))
for sb in range(0, 100, 1):
    if sb == na:
        break
        print(sb, "는 종료값이다")
    print(sb+1, end="  ")


# In[11]:


#p103.py
total = 0
for sb in range(1, 11,1):
    total = total + sb
print(total)


# In[12]:


#p106.py
sb=1
while sb < 4:
    print(sb)
    sb = sb + 1


# In[13]:


#p107_1.py
sb=0
while sb < 3:
    sb = sb + 1
    print(sb)


# In[14]:


#p107_2.py
for sb in range(0, 5, 1):
    print(sb, end="   ")
    
print("\n\n")
for sb in range(0, 10, 2):
    print(sb, end="   ")


# In[16]:


#p108_1.py
sb=0
while sb<5:
    print(sb, end="   ")
    sb=sb+1
print("\n\n")
sb=0
while sb <10:
    print(sb, end="   ")
    sb= sb + 2


# In[17]:


#p108_2.py

total = 0
for sb in range(1, 11, 1):
     total=total +  sb
print("1부터", sb,"까지의 총합은", total)


# In[18]:


#p108_3.py
total = 0
sb = 0
while sb < 11:
    total = total + sb
    sb = sb + 1
print("1부터", sb-1,"까지의 총합은", total)


# In[19]:


#p109.py
sb = 1
while True:
    print(sb)
    sb = sb + 1
    if sb > 3:
        break


# In[21]:


#p110.py
sb = 0
while True:
    sb = sb + 1    
    if sb > 3:
        break
    print(sb)


# In[22]:


#p116.py
for i in range(1, 10, 1):
    print(1, "*", i, "=", 1 * i )


# In[23]:


#p117.py
i=1
while i < 10:
    print(1, "*", i, "=", 1 * i )
    i = i + 1


# In[25]:


#p119_1.py
for i in range(1, 10, 1):
    print(1, "*", i, "=", 1 * i )
for i in range(1, 10, 1):
    print(2, "*", i, "=", 2 * i )


# In[27]:


#p119_2.py
i=1
while i < 10:
    print(1, "*", i, "=", 1 * i )
    i = i + 1
i=1
while i < 10:
    print(2, "*", i, "=", 1 * i )
    i = i + 1


# In[30]:


#p119_3.py
for i in range(1, 10, 1):
    print(1, "*", i, "=", 1 * i )
for i in range(1, 10, 1):
    print(2, "*", i, "=", 2 * i )
for i in range(1, 10, 1):
    print(3, "*", i, "=", 3 * i )
for i in range(1, 10, 1):
    print(4, "*", i, "=", 4 * i )
for i in range(1, 10, 1):
    print(5, "*", i, "=", 5 * i )


# In[31]:


#p121_1.py #책에 for j i n range(1,6,1) =>for j in range(1, 6, 1) 로 수정
for j in range(1, 6, 1):
    for i in range(1, 10, 1):
        print(j, "*", i, "=", j * i )


# In[32]:


#p121_2.py
j=1
while j < 6:
    i=1
    while i < 10:
        print(j, "*", i, "=", j * i )
        i = i + 1
    j = j + 1


# In[34]:


#p122.py
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i * j}")


# In[ ]:




