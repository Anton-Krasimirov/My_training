def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:# за всвеки нод минаваме през всички свързани
        dfs(child, graph, visited)

    print(node, end=' ')# отпечятай нода и остани на същия ред




'''описвам графа  с речник '''
graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}

visited = set()# отбелязваме кои са били вече посетени



for node in graph:# пускаме функцията за всеки един нод
    dfs(node, graph, visited)