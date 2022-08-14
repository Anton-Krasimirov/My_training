nodes = int(input())
# 8
# 1 -> 2 5 4
# 2 -> 1 3
# 3 -> 2 5
# 4 -> 1
# 5 -> 1 3
# 6 -> 7 8
# 7 -> 6 8
# 8 -> 6

graph = {}# {'1': ['2', '5', '4'], '2': ['1', '3'], '3': ['2', '5'], '4': ['1'], '5': ['1', '3'], '6': ['7', '8'], '7': ['6', '8'], '8': ['6']}
edges = []# [('1', '2'), ('1', '5'), ('1', '4'), ('2', '1'), ('2', '3'), ('3', '2'), ('3', '5'), ('4', '1'), ('5', '1'), ('5', '3'), ('6', '7'), ('6', '8'), ('7', '6'), ('7', '8'), ('8', '6')]

for _ in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))# tuples от всички ребра


def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()# събирам кои нодове са били посетени
    '''ако съм пуснал дфс от даден нод(source) и после по някакъв начин съм минал през destination, и destination е част от visited значи
     продължавам да имам път от source до destination след като съм махнал това ребро'''
    dfs(source, destination, graph, visited)

    return destination in visited

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)
    
    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))

    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(removed_edges)}")
for first, second in removed_edges:
    print(f'{first} - {second}')