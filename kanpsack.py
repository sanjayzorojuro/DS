def knapsack(n,capa,wig,pric):
    if n==0 or capa==0:
        return 0
    if (wig[n-1]>capa):
        return knapsack(n-1,capa,wig,pric)
    else:
        return max(pric[n-1]+knapsack(n-1,capa-wig[n-1],wig,pric),knapsack(n-1,capa,wig,pric))
    
weight=[7,3,4,5]
prices=[42,12,40,25]
n=4
capa=10

print(knapsack(n,capa,weight,prices))

    
