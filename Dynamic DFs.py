graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge: ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for i in graph[node]:
            dfs(i)

start = input("Enter starting node: ")
print("DFS Traversal:", end=" ")
dfs(start)
