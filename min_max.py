#this is a code to find the min max elements from a array using divide and conquer method.
from array import *

a=[]

def minmax(a,low,high):
    if low == high :
        return (a[low],a[high])
    elif high - low  == 1:
        if a[low] < a[high]:
            return (a[low],a[high])
        else:
            return (a[high],a[low])
    else:
        mid= (low+high) // 2 
        lmin,lmax = minmax(a,low,mid)
        rmin,rmax = minmax(a,mid+1,high)

        if lmin < rmin:
            min=lmin
        else:
            min=rmin
        if lmax > rmax:
            max=lmax
        else:
            max=rmax
        return(min,max)


n=int(input("Enter number of array elements:"))
for i in range(n):
    ele=int(input('Enter array elemenst:'))
    a.append(ele)

min,max=minmax(a,0,n-1)
print("The minimum element in the array is:",min)
print("The maximun element in the array is:",max)

        
