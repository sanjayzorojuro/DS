from array import *
import random
import time

def quicksort(a,low,high):
    if low<high:
        pi=partician(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)

def partician(a,low,high):
    pivot=a[low]
    i=low
    j=high

    while i<j:
        while a[i] <= pivot and i < high:
            i+=1
        while a[j] > pivot and j > low:
            j-=1
        if i < j:
            a[i],a[j]=a[j],a[i]
    a[low],a[j]=a[j],a[low]
    return j

a=array("i",[])

for i in range(5005):
    n=random.randrange(10000)
    a.append(n)

size=len(a)

print("The array before sorting :",a)
start=time.time()
print("Thw starting time is:",start)

quicksort(a,0,size-1)

print("The array after sorting :",a)    
end=time.time()
print("The ending time is:",end)

diff=end-start
print("The total time taken is :",diff)