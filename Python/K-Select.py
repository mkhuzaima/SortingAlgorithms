def Partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
def QuickSelect(arr,low,high,k):
    if low==high:
        return arr[low]
    else:
        Pivot_Index=Partition(arr,low,high)
        if k==Pivot_Index:
            return arr[k]
        elif k<Pivot_Index:
            high=Pivot_Index-1
        else:
            low=Pivot_Index+1
        return QuickSelect(arr,low,high,k)
math=[]
size=int(input("Enter Size of Array:"))
for i in range(0,size):
    j=int(input("Enter Elements of Array:"))
    math.append(j)
print(QuickSelect(math,0,len(math)-1,4))