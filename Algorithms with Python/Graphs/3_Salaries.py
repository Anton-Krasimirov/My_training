

nodes = int(input())
graph = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)


# 6
# NNNNNN
# YNYNNY
# YNNNNY
# NNNNNN
# YNYNNN
# YNNYNN

# print(graph)#  [[], [0, 2, 5], [0, 5], [], [0, 2], [0, 3]]

salaries = [None] * nodes#  пазим (заплатите) тук , тоест колко чайлд нода има всеки нод

'''[], [[], [0, 2, 5], [0, 5], [], [0, 2], [0, 3]], [None, None, None, None, None, None,]'''
def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1
    salary = 0 # междинна за да натрупваме в нея от чайлд нодовете на всеки чайлд
    for child in graph[node]:
        salary += dfs(child, graph, salaries)# [0, 2, 5], [[], [0, 2, 5], [0, 5], [], [0, 2], [0, 3]], [1, None, None, None, None, None,]
    salaries[node] = salary
    return salary

result = 0 # събира общия резултат
for node in range(nodes):# пълним стойности в salaries -> 0, 1, 2, 3, 4, 5
    salary = dfs(node, graph, salaries)
    result += salary

print(result)