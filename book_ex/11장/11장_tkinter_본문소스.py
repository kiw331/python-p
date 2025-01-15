#!/usr/bin/env python
# coding: utf-8

# In[2]:


#p278.py
import tkinter
otk = tkinter.Tk()
obtn = tkinter.Button(otk, text="click")
obtn.pack()
otk.mainloop()


# In[4]:


#p280_1.py
import tkinter
otk = tkinter.Tk()
otk.geometry("100x150")
obtn=tkinter.Button(otk, text="click")
obtn.pack()
otk.mainloop()


# In[6]:


#p280_2.py
import tkinter
otk = tkinter.Tk()
otk.geometry("100x150+400+400")
obtn=tkinter.Button(otk, text="click")
obtn.pack()
otk.mainloop()


# In[9]:


#p281.py
def hello():
    print("hello there")
from tkinter import *
otk = Tk()
obtn = Button(otk, text="click me", command=hello)
obtn.pack()
otk.mainloop()


# In[11]:


#p282_1.py
from tkinter import *
oroot = Tk()
obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")

obutton1.pack()
obutton2.pack()
obutton3.pack()
oroot.mainloop()


# In[12]:


#p282_2.py
from tkinter import *
oroot = Tk()
olabel1 = Label(oroot, text="적", bg="red", width = 20)
olabel2 = Label(oroot, text="녹", bg="green", width=20)
olabel3 = Label(oroot, text="파", bg="blue", width=20)
olabel1.pack()
olabel2.pack()
olabel3.pack()
oroot.mainloop()


# In[13]:


#p285.py
import tkinter
oroot = tkinter.Tk()
oent= tkinter.Entry(oroot)
oent.pack()
olabel =tkinter.Label(oroot, text="이름입력")
olabel.pack()
oroot.mainloop()


# In[14]:


#p286.py
import tkinter
oroot = tkinter.Tk()
ostring = tkinter.StringVar()
oentry = tkinter.Entry(oroot, textvariable = ostring)
oentry.pack()
olabel =tkinter.Label(oroot, textvariable = ostring)
olabel.pack()
oroot.mainloop()


# In[18]:


#p289_1.py  #책에 있는 grid() 내용 아래 코드로 교체해야함. 그림도 잘 못 들어감
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


# In[16]:


#p289_2.py
import tkinter
oroot = tkinter.Tk()
oroot.geometry("200x100+600+300")
obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")

obutton1.pack(side='left')
obutton2.pack(side='right')
obutton3.pack(side='top')
oroot.mainloop()


# In[17]:


#p289_3.py
import tkinter
oroot = tkinter.Tk()
oroot.geometry("200x100")
obutton1 = tkinter.Button(oroot, text="PUSH1")
obutton2 = tkinter.Button(oroot, text="PUSH2")
obutton3 = tkinter.Button(oroot, text="PUSH3")
obutton1.place(x=10, y=60)
obutton2.place(x=140, y=60)
obutton3.place(x=80, y=10)
oroot.mainloop()


# In[21]:


#p291_1.py
import tkinter
def order():
    print("주문하세요")    
root = tkinter.Tk()
btn=tkinter.Button(root, text="주문", command=order)
btn.pack()
root.mainloop()


# In[23]:


#p291_2.py
import tkinter
def msg():
    print("start tkinter")

root = tkinter.Tk()
mlabel = tkinter.Label(root, text="시작레이블")
mlabel.pack(side = 'top')

mbutton = tkinter.Button(root, text="시작버튼", command=msg)
mbutton.pack(side = 'bottom')
root.mainloop()


# In[27]:


#p294.py
import tkinter
oroot = tkinter.Tk()
radio_value = tkinter.IntVar()
radio_value.set(1)
lunch = {0: "A런치", 1:"B런치", 2:"C런치"}
orb1=tkinter.Radiobutton(oroot, text = lunch[0], variable = radio_value, value = 0)
orb1.pack()
orb2=tkinter.Radiobutton(oroot, text = lunch[1], variable = radio_value, value = 1)
orb2.pack()
orb3=tkinter.Radiobutton(oroot, text = lunch[2], variable = radio_value, value =2)
orb3.pack()
def buy():
    value = radio_value.get()
    print(lunch[value])

obutton = tkinter.Button(oroot, text = "주문", command = buy)
obutton.pack()
oroot.mainloop()


# In[25]:


#p298.py
import tkinter
oroot = tkinter.Tk()
coffee = {0:"아메리카노", 1:"라떼", 2:"카프치노", 3:"에스프레소"}
check_value={}
for i in range(len(coffee)):
    check_value[i]=tkinter.BooleanVar()
    ocheckbutton=tkinter.Checkbutton(oroot,variable=check_value[i], text=coffee[i])   
    ocheckbutton.pack(anchor="w")

def buy():
    for i in check_value:      
        if check_value[i].get() == True:
            print(coffee[i])
            
tkinter.Button(oroot, text="주문", command=buy).pack()
oroot.mainloop()


# In[2]:


#p299.py
'''프로그램 실행시 TclError: image " pyimage2" dosent exist 
는 이전코드에서 오류가 난 것이 계속 영향을 주어가 발생하는 
현상으로 jupyter notebook 에디터인 경우 restart 버튼을 실행하면 된다.
'''
import tkinter
oroot = tkinter.Tk()
oroot.geometry("200x100")
img1=tkinter.PhotoImage(file='pizzasb2.png')
img_label = tkinter.Label(oroot, image=img1)
img_label.place(x=-20, y=-20)
obutton1 = tkinter.Button(oroot, text="PUSH1")
obutton2 = tkinter.Button(oroot, text="PUSH2")
obutton3 = tkinter.Button(oroot, text="PUSH3")
obutton1.place(x=10, y=60)
obutton2.place(x=140, y=60)
obutton3.place(x=80, y=10)
oroot.mainloop()


# In[5]:


#p300
import tkinter as tk
root = tk.Tk()
options_list =['Option 1', 'Option 2', 'Option 3']
selected_option=tk.StringVar()
selected_option.set(options_list[0])

option_menu = tk.OptionMenu(root, selected_option,*options_list)
option_menu.pack()
root.mainloop()


# In[ ]:




