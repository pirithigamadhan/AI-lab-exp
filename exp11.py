colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = {}

def solve(node):
    if node == len(graph):
        return True

    region = list(graph)[node]

    for color in colors:
        if all(result.get(n) != color for n in graph[region]):
            result[region] = color
            if solve(node + 1):
                return True
            del result[region]

    return False

solve(0)
print(result)