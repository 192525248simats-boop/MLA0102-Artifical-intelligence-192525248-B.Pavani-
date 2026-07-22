import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': []
}

h = {'A':4, 'B':2, 'C':1, 'D':0}

queue = [(0, 'A')]
visited = []

while queue:
    cost, node = heapq.heappop(queue)

    if node not in visited:
        visited.append(node)
        print(node, "Cost =", cost)

        for next_node, weight in graph[node]:
            heapq.heappush(queue, (cost + weight + h[next_node], next_node))
