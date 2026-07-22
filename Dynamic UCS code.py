import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

h = {'A':3, 'B':2, 'C':1, 'D':0}

queue = [(h['A'], 'A')]
visited = []

while queue:
    value, node = heapq.heappop(queue)

    if node not in visited:
        visited.append(node)

        for i in graph[node]:
            heapq.heappush(queue, (h[i], i))

print("Best First Search:", visited)
