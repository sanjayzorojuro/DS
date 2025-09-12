from array import *
import random
import time

def mergesort(a,low,high):
    if(low<high):
        mid = (low+high) // 2
        mergesort(a,low,mid)
        mergesort(a,mid+1,high)
        merge(a,low,mid,high)

def merge(a,low,mid,high):
    n1= mid - low + 1
    n2= high - mid

    left=[0] * (n1)
    right=[0] * (n2)

    for i in range(0,n1):
        left[i] = a [low + i]
    for  j in range(0,n2):
        right[j] = a [mid+1+j]

    i=j=0
    k=low

    while i<n1 and j<n2:
        if left[i] <= right[j]:
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
        k+=1
    while (i<n1):
        a[k]=left[i]
        i+=1
        k+=1
    while (j<n2):
        a[k]=right[j]
        j+=1
        k+=1

a=array('i',[])

for i in range(5005):
    n=random.randrange(5000)
    a.append(n)

size=len(a)

print("Array before sorting:",a)
start=time.time()
print("The starting time is :",start)

mergesort(a,0,size-1)

print("Array after sorting:",a)
end=time.time()
print("The ending time is:",end)

diff=end-start
print("The total time taken to complete the sorting is:",diff)
    
