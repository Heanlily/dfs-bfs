graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['C','B','F','E'],
    'E':['C','D'],
    'F':['D']
}

def bfs(graph,s):
    queue=[]
    queue.append(s)
    SEEN=set()
    SEEN.add(s)
    while queue:
        ver=queue.pop(0)
        nodes=graph[ver]
        for w in nodes:
            if w not in SEEN:
                queue.append(w)
                SEEN.add(w)
        print(ver)
print(bfs(graph,'A'))

def dfs(graph,s):
    queue=[]
    order=[]
    queue.append(s)
    while queue:
        v=queue.pop()
        order.append(v)
        for w in graph[v]:
            if w not in order and w not in queue:
                queue.append(w)
        print(v)

print(dfs(graph,'A'))
