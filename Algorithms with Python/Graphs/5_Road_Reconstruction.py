nodes_count = int(input())
edges_count = int(input())
# 5
# 5
# 1 - 0
# 0 - 2
# 2 - 1
# 0 - 3
# 3 - 4

graph = []# [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
[graph.append([]) for x in range(nodes_count)]

edges = []# съхранява ребрата, може да е сет за да няма дублаж

for _ in range(edges_count):#  за да се получат позициите на ребрата за всеки нод при ненасочен граф
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)# от сорс към дестинейшън
    graph[second].append(first)# от дестинейшън към сорс
    edges.append((min(first, second), max(first, second)))# добавям ги сортирани по възходящ ред заради условието за принт накрая

important_streets = []# ще съдържа важните ребра
'''ще извадим от графа ребро и в двете му посоки и с дфс от 0 индекс ще проверим дали можем да стигнем до всеки нод , 
ако не можем да стигнем ще го добавим като важен път'''

'''получаваме нод , проверяваме дали е посетен , ако не отбелязваме че минаваме през него и също и през неговите деца с друго дфс'''
def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)
    
    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print(f"Important streets:")
for edge1, edge2 in important_streets:
    print(edge1, edge2)