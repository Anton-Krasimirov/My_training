'''Обиколка на всички нодове по път с минимална стойност, алгоритъм на Kruskal'''

nodes = int(input())
edges = int(input())

graph = [] # [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight)) # ползваме tuple вместо class

parent = [num for num in range(nodes)] # [0, 1, 2, 3]


def first_root(parent, node): # [0, 1, 2, 3], 0
    while node != parent[node]:
        node = parent[node]
    return node

total_cost = 0
for first, second, weight in sorted(graph, key=lambda x: x[2]): # сортираме по третия елемент[(2, 3, 4), (0, 3, 5), (0, 2, 6), (0, 1, 10), (1, 3, 15)]
    first_node_root = first_root(parent, first)
    second_node_root = first_root(parent, second)

    if first_node_root == second_node_root:
        continue

    parent[first_node_root] = second_node_root # нужно е заради проверката на рут стойностите по горе
    total_cost += weight

print(f'Total cost: {total_cost}')