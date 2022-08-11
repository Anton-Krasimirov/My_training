
from queue import PriorityQueue

class Edge():
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
'''речник за всеки ключ пазим инстанция на клас със начало, краи и тежест на реброто'''
graph = {}# {0: [<__main__.Edge object at 0x0000017143B0A1F0>, <__main__.Edge object at 0x0000017143B29730>], 6: [......]}
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))# добавям инстанция на класа в празни масиви в речника за конкретния нод


start = int(input())
target = int(input())

'''понеже не са подредени нодовете за да ползваме индекси , ще се вземе броя на най-големия нод и ще се напрявят толкова бр '''
max_node = max(graph.keys())
'''правим два масива един за стойности на пътя и един за предходните нодове'''
distance = [float('inf')] * (max_node + 1)# стойностите са положителна безкрайност за да са винаги по-големи пържоначално [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

parent = [None] * (max_node + 1)# [None, None, None, None, None, None, None, None, None, None, None, None]
distance[start] = 0# задаваме индекса от които тръгваме 0 защото той нама как да има стойност


pq = PriorityQueue()# приоритетна опашка , винаги ще дава най малката стойност, ще добавяме tuples(дистанция, старт) опашката ще сортира по първия
# елемент и затова слагаме първо дистанцията , понеже искаме да проверяваме нейната стойност

pq.put((0, start))

while not pq.empty():#  докато в опашката има стойности
    min_distance, node = pq.get()# опашката ще върне най ниската стойност от колекцията и я маха
    if node == target:
        break
    for edge in graph[node]:# минаваме през клас инстанциите на конкретния нод
        new_distance = min_distance + edge.weight # смятаме стойноста на пътя за да я сравним и евентуално да я сменим
        if new_distance < distance[edge.destination]:#  проверяваме коя е по-малка
            distance[edge.destination] = new_distance# променяме стойноста в листа на нода който отговаря на дистанцията на този нод, е следващия нод
            parent[edge.destination] = node # поставяме в листа с изминалите нодове попнатия нод (родителя)
            pq.put((new_distance, edge.destination))# добавяме в опашката tuple с новата тежест и нода, тя ще ни връща по-ниската тежест с приоритет

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = []
    node = target
    while node is not None:
        path.append(node)# добавяме в опашката отпред за да ги принтне от начало
        node = parent[node]# вирвим по списъка с посетени в обратен ред , там са отбелязани паренд нодовете на посетените
        path_by_nodes = reversed(path)
    print(*path_by_nodes, sep=' ')
