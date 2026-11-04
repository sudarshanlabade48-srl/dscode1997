A pizza shop receives multiple orders from several locations. Assume that one pizza boy is
tasked with delivering pizzas in nearby locations, which is represented using a graph. The
time required to reach from one location to another represents node connections. Solve the
problem of delivering a pizza to all customers in the minimum time. Use appropriate data
structures


V = int(input("Enter number of customers: "))
E = int(input("Enter number of routes: "))

G = [[0] * V for _ in range(V)]

for i in range(E):
    v1 = int(input("Enter first location : "))
    v2 = int(input("Enter second location : "))
    time = int(input("Enter delivery time: "))

    if v1 < 0 or v1 >= V or v2 < 0 or v2 >= V:
        print("Invalid location number")
        exit()

    if time <= 0:
        print("Delivery time must be positive")
        exit()

    G[v1][v2] = time
    G[v2][v1] = time

print("\nGRAPH:")

for row in G:
    print(row)

distance = [float("inf")] * V
visited = [0] * V

distance[0] = 0

for count in range(V):
    minimum = float("inf")
    current = -1

    for i in range(V):
        if visited[i] == 0 and distance[i] < minimum:
            minimum = distance[i]
            current = i

    if current == -1:
        break

    visited[current] = 1

    for i in range(V):
        if G[current][i] != 0 and visited[i] == 0:
            new_time = distance[current] + G[current][i]

            if new_time < distance[i]:
                distance[i] = new_time

print("\nMINIMUM DELIVERY TIME:")

for i in range(1, V):
    if distance[i] == float("inf"):
        print("Pizza Shop -> Customer", i, "= No route available")
    else:
        print("Pizza Shop -> Customer", i, "=", distance[i], "minutes")
