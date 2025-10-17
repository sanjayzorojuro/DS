def findsubset(s,d):
    def rec(index,csum,cset):
        if csum==d:
            subset.append(list(cset))
            return
        if csum > d or index == len(ele):
            return
        rec(index+1,csum+ele[index],cset+[ele[index]])
        rec(index+1,csum,cset)

    subset=[]   
    ele=list(s)
    rec(0,0,[])
    return subset
s= set(map(int,input("Enter comma separated values:").split(',')))
d=int(input("Enter the weight"))
res=findsubset(s,d)
if res:
    print("THe subset for :",d)
    for subset in res:
        print(subset)
else:
    print("There is no subset for ",d)