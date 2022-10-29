#!/usr/bin/env python
# coding: utf-8

# In[6]:


def CountingSort(arr1):

    minimum = min(arr1)
    k = (max(arr1) - minimum)+1
    count = [0]*(k)
    output = [0]*len(arr1)

    for i in range(len(arr1)):
        j =arr1[i]
        count[j-minimum] += 1

    for i in range(1,k):
        count[i] += count[i-1]

    for i in range(len(arr1)-1,-1,-1):
        j = arr1[i]
        count[j-minimum] -=1
        output[count[j-minimum]] = arr1[i]

    return output
math=[]
size=int(input("Enter Size of Array:"))
for  i in range(0,size):
    math1=int(input("Enter Elements of Array:"))
    math.append(math1)
print(CountingSort(math))


# In[ ]:




