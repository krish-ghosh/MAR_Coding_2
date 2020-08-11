#!/usr/bin/env python
# coding: utf-8

# In[1]:


low = input()
high = input()

def is_kaprekar_number(num):
    square = str(num*num)  
    mid = len(square)//2
  
    num1 = 0
    try: 
        num1 = int(square[0:mid])
    except:
        pass
  
    num2 = 0
    try: 
        num2 = int(square[mid:])
    except:
        pass
  
    if num1+num2 == num:
        return True
  
    return False
  
found = False
for i in range(int(low), int(high)+1):
    if is_kaprekar_number(i):
        found = True
        print(i, end=" ")
if found == False:
    print("INVALID RANGE")  

