def solutiona(b):
    for row in b:
        print("".join("Q" if col else"."for col in row))

    print()

def is_safe(b,row,col,n):
    for i in range(n):
        if b[i][col]:
            return False
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if b[i][j]:
            return False
    for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
        if b[i][j]:
            return False
    return True

def solve_n(b,row,n,sol):
    if row==n:
        solution=[row[:]for row in b]
        sol.append(solution)

    for col in range(n):
        if is_safe(b,row,col,n):
            b[row][col]=1
            solve_n(b,row+1,n,sol)
            b[row][col]=0

def nqueen(n):
    b=[[0 for _ in range(n)]for _ in range(n)]
    sol=[]
    solve_n(b,0,n,sol)
    return sol

n=int(input("Enter a number"))
res=nqueen(n)
print(f"the queens for {n} is :{len(res)}")
for idx,solu in enumerate(res,start=1):
    print(f"The solutio is {idx}")
    solutiona(solu)
