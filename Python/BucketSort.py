#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
def InsertionSort(arr):
    size = len(arr)

    for j in range(1, len(arr)):
        key = arr[j] 
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

def BucketSort(arr,size):

    bucket = []
    for _ in range(size):
        bucket.append([])

    for i in range(0,size):
        n = math.floor(arr[i]*size)
        bucket[n].append(arr[i])

    for i in range(0,len(bucket)):
        InsertionSort(bucket[i])

    index = 0
    for i in range(0,len(bucket)):
        array = bucket[i]
        for j in range(0,len(array)):
            arr[index] = bucket[i][j]
            index += 1

arr=[]
size=int(input("Enter Size of Array:"))
for  i in range(0,size):
    math1=int(input("Enter Elements of Array:"))
    arr.append(math1)
print(BucketSort(arr,len(arr)))

