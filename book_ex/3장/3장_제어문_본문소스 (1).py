#!/usr/bin/env python
# coding: utf-8

# In[2]:


#p66.py
na = 10
nb = 20
if na <= nb:
    print("na : ", na, "nb : ", nb)
    print(nb, "는", na, "보다 크다")
print("프로그램 종료")


# In[3]:


#p68.py
print(True and True)
print(True and False)
print(False or False)
print(False or True)


# In[1]:


#p69.py
print(9>4 and 3>2)
print(9<4 and 3>2)
print(9<4 or 3<2)
print(9<4 or 3>2)


# In[2]:


#p71.py
na = 21
if na % 2 ==0:
    print(na, "짝수")
print("if문 종료 됨")


# In[3]:


#p73.py
na = 21
if na % 2 ==0:
    print(na, "짝수")
else:
    print(na, "홀수")
print("if문 종료 됨")


# In[4]:


#p76.py
tscore = 700
if tscore > 900:
    print("당신의 토익점수는", tscore, "상위권")
elif tscore > 700:
    print("당신의 토익점수는", tscore, "중위권")
else:
    print("당신의 토익점수는", tscore, "하위권")
print("if 문 종료됨")


# In[5]:


#p78.py
print("월요일부터 일요일 중 영어로 번역하고 싶은 요일을 입력하세요")
yoil = input()
if yoil == "월요일":
    print("monday")
elif yoil == "화요일":
    print("tuesday")
elif yoil == "수요일":
    print("wednesday")
elif yoil == "목요일":
    print("thursday")
elif yoil == "금요일":
    print("friday")
elif yoil == "토요일":
    print("saturday")
elif yoil == "일요일":
    print("sunday")
else:
    print("한글 요일을 잘못 입력했습니다")


# In[6]:


#p79.py
score = float(input("수학점수를 입력하세요"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade="F"
    
print("수학 성적은", grade, "입니다")
    


# In[7]:


#p80.py
score = float(input("수학점수를 입력하세요"))
if score >= 60:
    if score >= 70:
        if score >= 80:
            if score >= 90:
                grade="A"
            else:
                grade="B"
        else:
            grade="C"
    else:
        grade="D"
else:
    grade = "F"
    
print("수학 성적은", grade, "입니다")


# In[ ]:




