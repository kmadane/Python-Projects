#!/usr/bin/env python
# coding: utf-8

# In[8]:


#2
for i in range(1,21):
    for j in range(i+1,21):
        if (i+j)%2==0:
            print("Sum is Even,Pair is: ",i,j,"The sum is: ",i+j)
        else:
            print("For",i,j,"Nothing can be done")


# In[21]:


#1
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],'rishabh_',5+5j],4000]
print(x[4][0],x[4][1])


# In[26]:


#3
x='hello&*$$world'
c1=0
c2=0
c3=0
for char in x:
    if char=='&':
        c1=c1+1
    elif char=='*':
        c2=c2+1
    elif char=='$':
        c3=c3+1
print("&:",c1," ", "*:",c2," ","$:",c3)
        


# In[27]:


#4
for i in range(1,51):
    if (i**3)%2!=0:
        print("The numbers are: ",i)


# In[33]:


#6
x='Hello world I am learning Python'
words=x.split()
for i in words:
    print("For: ",i,"length of: ",i, "is: ",len(i))


# In[60]:


#7
x=[12,'xyz',10,9]
all(isinstance(i,int) for i in x)


# In[62]:


#5
x=[1,2,3,4,5]
new_list=x.copy()
new_list


# In[64]:


#5
x=[33,66,99,3,12]
newlist = [i for i in x if i%3==0]
newlist


# In[ ]:




