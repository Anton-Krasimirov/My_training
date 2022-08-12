'''Алгоритъма представлява подобие на Dijkstra но тук имаме обхождане на всички нодове колкото е броя им минъс един път
и след това првим в отделен цикъл още едно обхождане , ако при него се намери по-добра стойност значи някъде имаме цикъл в
 графа . Алгоритъма се използва за намиране на най-кратък път в граф с отрицателни стойности на ребра или дали има цикъл
 в графа'''
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight



nodes = int(input())
edges = int(input())
graph = [] # 1 2 8 | 1 3 10 | 2 4 1 | 3 6 2 | 4 3 -4 | 4 6 -1 | 6 5 -2 | 5 3 1  съхраняваме като ребра
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1) # +1 заради нулевия индекс , ще остане неизползван  [inf, 0, 8, 5, 9, 5, 7]-  накрая
parent = [None] * (nodes + 1)
distance[start] = 0

for _ in range(nodes - 1): # итерации с една по-малко от броя нодове , според условието на алгоритъма
    updated = False
    for edge in graph: # мини през всички ребра в графа , там ги съхраняваме като ребра
        if distance[edge.source] == float('inf'): # няма резултат за нода от който реброто излиза, не можем да правим проверка коректна
            continue
        new_distance = distance[edge.source] + edge.weight # запазената информация за нода плюс стойноста на реброто
        if new_distance < distance[edge.destination]: # запазената стойност за дестинейшън нода
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source #
            updated = True

    if not updated:# съкращава итерациите , да не са всички , ако няма намерен по-добър път при някоя следващите са излишни
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[target])