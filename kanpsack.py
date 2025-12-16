def knapsacks(n,c,w,p):
    if n == 0 or c == 0:
        return 0 
    if w[n-1] > c : 
        return knapsacks(n-1,c,w,p)
    else:
        return max(p[n-1]+knapsacks(n-1,c-w[n-1],w,p),knapsacks(n-1,c,w,p))
    
p = [10,20,30,50]
w = [1,2,3,4]
c = 6
n = 4


print("The price is:",p)
print("The weight is:",w)
print("The capacity is:",c)

print()
print("Optimal solution:")  
print(knapsacks(n,c,w,p))

