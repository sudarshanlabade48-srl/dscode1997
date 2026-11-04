Title : Consider a particular area in your city. Note the popular locations 0, 1, 2 . .
in that area. Assume these locations represent nodes of a graph. If there is a route
between two locations, it is represented as connections between nodes. Find out the
sequence in which you will visit these locations, starting from (say 0) using DFS.
Represent a given graph using an adjacency matrix to perform DFS.


def dfs(matrix, start, visited):
    print(start, end=" ")
    visited[start] = 1

    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited)


print("DEPTH FIRST SEARCH")

nodes = int(input("ENTER TOTAL NUMBER OF NODES: "))
edges = int(input("ENTER NUMBER OF EDGES: "))

matrix = []

for i in range(nodes):
    row = [0] * nodes
    matrix.append(row)

print("\nADJACENCY MATRIX:")
for row in matrix:
    print(row)

print("\nENTER THE EDGES:")

for x in range(edges):
    a = int(input("ENTER THE STARTING NODE: "))
    b = int(input("ENTER THE END NODE: "))

    matrix[a][b] = 1
    matrix[b][a] = 1

print("\nADJACENCY MATRIX AFTER ADDING EDGES:")
for row in matrix:
    print(row)

visited = [0] * nodes

start = int(input("ENTER THE STARTING NODE FOR DFS: "))

print("\nDFS TRAVERSAL:")
dfs(matrix, start, visited)
print()




def bfs(adj, start):
    visited = [0] * len(adj)
    queue = [start]
    visited[start] = 1

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1



print("BREADTH FIRST SEARCH")

nodes = int(input("ENTER TOTAL NUMBER OF NODES: "))
edges = int(input("ENTER NUMBER OF EDGES: "))

adj = [[] for _ in range(nodes)]

print("\nENTER THE EDGES:")

for _ in range(edges):
    a = int(input("ENTER THE STARTING NODE: "))
    b = int(input("ENTER THE END NODE: "))

    adj[a].append(b)
    adj[b].append(a)

print("\nADJACENCY LIST:")

for i in range(nodes):
    print(i, "->", adj[i])

start = int(input("\nENTER START NODE: "))

print("BFS TRAVERSAL:")
bfs(adj, start)
print()




