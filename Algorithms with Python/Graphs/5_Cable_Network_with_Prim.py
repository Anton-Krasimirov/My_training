'''имаме някаква мрежа от нодов , трябва да се разшири по даден бюджет , като за него трябва да свържем колкото се може повече
нодове саобразявайки се с цената ина ребрата ни която ни е дадена( Prim or Kruskal)'''
from queue import PriorityQueue
class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first

    def __gt__(self, other):
        return self.weight > other.weight

budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

tree = set() # добавяме първо свързаните нодове , и към тях ще добавяме новите свързани
for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(first, second, weight))

    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)

pq = PriorityQueue() # добавяме всички свързани ребра на нодовет налични в дървото и после за всеки новодобавен
for node in tree:
    for edge in graph[node]:
        pq.put(edge)

budger_used = 0
while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.first in tree and min_edge.second not in tree:
        non_tree_node = min_edge.second
    elif min_edge.first not in tree and min_edge.second in tree:
        non_tree_node = min_edge.first

    if non_tree_node is None:
        continue

    if budger_used + min_edge.weight > budget: # брейкваме защото ако не можем да добавим това ребро , и всяко следващо е по-голямо заради сортировката
        break
    budger_used += min_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)


print(f'Budget used: {budger_used}')