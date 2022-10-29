#!/usr/bin/env python
# coding: utf-8

# In[4]:


def digitCounter(array):
    value = max(array)
    value = str(value)
    return len(value)

def findElement(value,digit):
    digit = digit+1
    output = 0
    for i in range(digit):
        output = value%10
        value = value//10
    return output


def RadixSort(array,digits):
    i=0
    while i<digits:
        buckets = []
        for _ in range(10):
            buckets.append([])

        for j in range(0,len(array)):
            value = findElement(array[j],i)
            buckets[value].append(array[j])

        index = 0
        for ind in range(0,len(buckets)):
            arr = buckets[ind]
            for index in range(0,len(arr)):
                array[index] = buckets[ind][index]
                index += 1
        i+=1
math=[]

size=int(input("Enter Size of Array:"))
for  i in range(0,size):
    math1=int(input("Enter Elements of Array:"))
    math.append(math1)
digits = digitCounter(math)
print(digits)
print(RadixSort(math,digits))


