#Following is the code for BFS.
graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':['f'],
    'f':[],
    'g':[]
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="\t")
        for neig in graph[m]:
            if neig not in visited:
                visited.append(neig)
                queue.append(neig)
                
print("Adjency list of the given graph is:")
for k,v in graph.items():
    print(f"{k}:{v}")

print("Here is the following BFS graph")
bfs(visited,graph,'a')
