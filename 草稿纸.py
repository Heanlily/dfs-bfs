adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

def dfs_recursive(graph, vertex, path):
    path+=[vertex]
    for i in graph[vertex]:
        if i not in path:
            dfs_recursive(graph,i,path)
    return path


def dfs_iterative(graph, start):
    path=[start]
    res=[]
    while path:
        node=path.pop()
        if node in res:
            continue
        res.append(node)
        for i in graph[node]:
            if i not in res:
                path.append(i)
    return res

def bfs_iterative(graph, start):
    path=[start]
    res=[]
    seen={start}
    while path:
        node=path.pop(0)
        res.append(node)
        for i in graph[node]:
            if i not in seen:
                path.append(i)
                seen.add(i)
    return res




print(dfs_recursive(adjacency_matrix, 1,[]))

print(dfs_iterative(adjacency_matrix, 1))

print(bfs_iterative(adjacency_matrix, 1))