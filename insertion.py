from array import *

def ins(a,n):
    for i in range(n):
        v=a[i]
        j=i-1
        while j>=0 and a[j]>v:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=v
    return a

a=array("i",[])
n=int(input("Enter the number of elements in the array:"))
for i in range(n):
    ele=int(input("Enter the array elements:"))
    a.append(ele)

print("The array before sorting:",a)
print("The array after sorting",ins(a,n))
