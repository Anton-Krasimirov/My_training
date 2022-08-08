from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source]) # deque([1])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            continue
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node
    return parent


def find_path_size(parent, destination):
    node = destination
    size = 0
    while node is not None:  # ще вървим назад в parent масива за да образуваме изминатия път , като взимаме на всеки парент парента
        node = parent[node]
        size += 1
    return size -1


nodes = int(input())
pairs = int(input())

graph = {}


for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children#  заместваме получения лист на индекса в графа


for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]
    '''трябв да търсим най кратък път от отчка до точка , ползва се BFS'''

    parent = find_shortest_path(graph, source, destination)

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parent, destination)
    print(f'{{{source}, {destination}}} -> {size}')