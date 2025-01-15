#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p41.py
na=10
nb=20.2
sa="python"
print("na변수값", na)
print("nb변수값", nb)
print("nc변수값", na)


# In[3]:


#p41_2.py
nc=30
nd=40
print("nc = ", nc, "nd = ", nd)
nd=nc
print("nc = ", nc, "nd = ", nd)


# In[4]:


#p43.py
print(5+2)
na = 5 + 2
print(na)


# In[7]:


#p44_45.py #책에서 코드 a->na, b->nb로 수정해야 함.
na = 20
nb = 5
result = na + nb
print(na, "+", nb, "=", result)
print("na값", na, "더하기 nb값", nb, "의 결괏값은",na+nb,"이다.")
result = na - nb
print(na, "-", nb, "=", result, "이다" )
result = na * nb
print(na, "*", nb, "=", result, "이다")
result = na / nb
print(na, "/", nb, "=", result, "이다")


# In[9]:


#p46.py
print("첫 번째 점수를 입력하세요")
ra = input()#커서가 깜박이면 20을 입력 후 엔터키를 누른다. 
rb = input("두 번째 정수를 입력하세요")#커서가 깜박이면 5를 입력 후 엔터키를 누른다. 
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")


# In[11]:


#p47.py
print("첫 번째 점수를 입력하세요")
ra = int(input())#커서가 깜박이면 20을 입력 후 엔터키를 누른다. 
rb = int(input("두 번째 정수를 입력하세요"))#커서가 깜박이면 5를 입력 후 엔터키를 누른다. 
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")


# In[13]:


#p48.py
a = input("첫 번째수를 입력하세요.")
print("변수 a를 갖고 있는 위의 명령문과 변수를 갖고 있지 않은 아래의 명령문을 비교해봅시다")
input("두 번째 정수를 입력하세요")
print("첫 번째 입력한 정수의 값은", a, "입니다")
print("두 번째 입력한 정수의 값은 어떻게 표시할지 모르겠네요")


# In[14]:


#p60_1.py
print("첫 번째 점수를 입력하세요")
ra = input()#커서가 깜박이면 20을 입력 후 엔터키를 누른다. 
rb = input("두 번째 정수를 입력하세요")#커서가 깜박이면 5를 입력 후 엔터키를 누른다. 
ra = int(ra)
rb = int(rb)
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")
rd = ra - rb
print(ra, "-", rb, "값은", rd, "이다")


# In[16]:


#p60_2.py
print("첫 번째 점수를 입력하세요")
ra = input()#커서가 깜박이면 20을 입력 후 엔터키를 누른다. 
rb = input("두 번째 정수를 입력하세요")#커서가 깜박이면 5를 입력 후 엔터키를 누른다. 
print(type(ra))
print(type(rb))
ra = int(ra)
rb = int(rb)
print(type(ra))
print(type(rb))
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이다")
rd = ra - rb
print(ra, "-", rb, "값은", rd, "이다")


# In[17]:


#p51.py
a = input("실수를 입력하세요.")
b = input("두 번째 실수를 입력하세요")
result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)


# In[18]:


#p51_실수형변화코드.py
a = input("실수를 입력하세요.")
b = input("두 번째 실수를 입력하세요")
a=float(a)
b=float(b)
result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)


# In[ ]:




