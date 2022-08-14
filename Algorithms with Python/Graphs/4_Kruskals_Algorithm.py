'''търси гора в граф, по най-ниски стойностн на ребро за всяко дърво(ако има повече от 1), без цикъл в дървото, обхващащо всеки нод'''
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())
graph = []# (0, 3, 9)(0, 5, 4)(0, 8, 5)(1, 4, 8)(1, 7, 7)(2, 6, 12)(3, 5, 2)(3, 6, 8)(3, 8, 20)(4, 7, 10)(6, 8, 7)

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node) # така ще се получи най-голямата стойност на нод , трябва ми за ренджа на parent масива

parent = [num for num in range(max_node + 1)] # [0, 1, 2, 3, 4, 5, 6, 7, 8] всеки нод да си е парънт, тук ще заместваме на индексите слагаме руут нод


def find_root(parent, node): # трябва да връща roota на node, ще върви назад по парент нода си до рута, и го подава
    while node != parent[node]:
        node = parent[node]
    return node


forest = []
for edge in sorted(graph, key=lambda e: e.weight): # сортирания тежесст на реброто граф (3, 5, 2) (0, 5, 4) (0, 8, 5) ....
    first_node_root = find_root(parent, edge.first) # find_root(parent, 3) подавам нод , връща ми неговия рут
    second_node_root = find_root(parent, edge.second) # find_root(parent, 5) ако на двата са различни рутове трябва да ги свържа
    if first_node_root != second_node_root: # ако е вярно условието трябва да закачим дърветата едно с друго понеже нодовете са на едно ребро
        parent[first_node_root] = second_node_root # заместваме индекса рута на сорс нода ,със рут нода на дестинейшън нода
        forest.append(edge) # подреждаме инстанциите за принтване в правилен ред

for edge in forest:
    print(f'{edge.first} - {edge.second}')