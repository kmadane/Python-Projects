#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=input("Enter a number: ")
b=input("Enter another number: ")
if a<b:
    print("True")
else:
    print("False")


# In[8]:


a=70
b=50
c=100
if a>b and a>c:
    print("A is max")
elif b>a and b>c:
    print("B is max")
elif c>a and c>b:
    print("C is max")


# In[10]:


def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print (x),
    counter += 1
    if (counter > 10): break 
print


# In[16]:


#Stock Price Problem

def StockPicker(arr): 
  
  max_profit = -1
  buy_price = 0
  sell_price = 0
  
  # this allows our loop to keep iterating the buying
  # price until a cheap stock price is found
  change_buy_index = True
  
  # loop through list of stock prices once
  for i in range(0, len(arr)-1):
    
    # selling price is the next element in list
    sell_price = arr[i+1]
    
    # if we have not found a suitable cheap buying price yet
    # we set the buying price equal to the current element
    if change_buy_index: 
      buy_price = arr[i]
    
    # if the selling price is less than the buying price
    # we know we cannot make a profit so we continue to the 
    # next element in the list which will be the new buying price
    if sell_price < buy_price:
      change_buy_index = True 
      continue
    
    # if the selling price is greater than the buying price
    # we check to see if these two indices give us a better 
    # profit then what we currently have
    else:
      temp_profit = sell_price - buy_price
      if temp_profit > max_profit:
        max_profit = temp_profit
      change_buy_index = False
      
  return max_profit

arr=[150,10,50,100,1,18,95]

print ("Max Profit: ", StockPicker(arr))


# In[37]:


# Python program to demonstrate accessing of 
# Counter elements 
#Find driver's room
from collections import Counter 
  
# Create a list 
z = [1,1,1,1,1,2,2,2,2,2,8,8,8,8,8,10,10,10,10,10,5]
d = Counter(z) 
print("No of Family Members: ",d) 

type(d)


rev = {v: k for k, v in d.items()}

#Then you use that like any other dictionary:

key_whose_count_is_1 = rev[1]
print("Driver's Room is: ",key_whose_count_is_1)


# In[ ]:




