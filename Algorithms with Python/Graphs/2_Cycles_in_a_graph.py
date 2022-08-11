'''дали графа е цикличен или е ацикличен'''
'''DFS алгоритъм за топологично сортиране е по подходящ за хващане само на цикли'''

def dfs(node, graph, visited, cycles):# първо извикване А, {'A': ['F'], 'F': ['D'], 'D': ['A']}, set(), set()
    if node in cycles:# нода образува цикъл
        raise Exception
    if node in visited:# нода е посетен само
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}

while True:# създаване на графа
    line = input()
    if line == 'End':
        break

    source, destination = line.split('-')# начална и крайна точка на реброто
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)# за да се образуват нодовете с посоките на където сочат ребрата

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')