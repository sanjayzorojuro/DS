from array import *

n=int(input("Enter the length of the array:"))
a=[]

for i in range(n):
    ele=int(input("Enter the array elements:"))
    a.append(ele)

print("The array elements before sorting is:",a)

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]

print("The array elemnts after sorting is:",a)
