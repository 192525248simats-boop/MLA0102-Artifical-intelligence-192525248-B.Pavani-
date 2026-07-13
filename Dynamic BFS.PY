from collections import deque

graph = {}

n = int(input("Enter number of edges: "))

print("Enter the edges:")
for i in range(n):
    u, v = input().split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting node: ")

visited = set()
queue = deque([start])

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
