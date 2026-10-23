def astar(graph, h, start, goal):
    q = [(h[start], start)]
    cost = {start: 0}

    while q:
        q.sort()
        f, node = q.pop(0)
        print(node, end=" ")

        if node == goal:
            return

        for n, w in graph[node]:
            g = cost[node] + w
            if n not in cost or g < cost[n]:
                cost[n] = g
                q.append((g + h[n], n))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

astar(graph, h, 'A', 'D')