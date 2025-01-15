#!/usr/bin/env python
# coding: utf-8

# In[3]:


#p324.py
vb = "변수 vb에 저장된 내용"
fwobj = open("fa.txt", "w")
b=fwobj.write(vb)
print(b)
fwobj.close()


# In[4]:


#p325.py
frobj = open("fa.txt", 'r')
vb = frobj.read()
frobj.close()
print(vb)


# In[ ]:




