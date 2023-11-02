from collections import defaultdict
import time

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isBCUtil(self, u, visited, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                if self.isBCUtil(v, visited, parent, low, disc):
                    return True
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    return True

                if parent[u] != -1 and low[v] >= disc[u]:
                    return True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

        return False

    def isBC(self):
        begintime = time.time_ns()
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        if self.isBCUtil(0, visited, parent, low, disc):
            endtime = time.time_ns()
            print(f"Execution time: {endtime - begintime} nanoseconds")
            return False

        if any(i == False for i in visited):
            endtime = time.time_ns()
            print(f"Execution time: {endtime - begintime} nanoseconds")
            return False
        endtime = time.time_ns()
        print(f"Execution time: {endtime - begintime} nanoseconds")
        return True

# Rest of your code remains the same

g1 = Graph(2)
g1.addEdge(0, 1)
print("Yes" if g1.isBC() else "No")

g2 = Graph(10)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(2, 4)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(2, 4)

print("Yes" if g2.isBC() else "No")

g3 = Graph(3)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
print("Yes" if g3.isBC() else "No")

g4 = Graph(5)
g4.addEdge(1, 0)
g4.addEdge(0, 2)
g4.addEdge(2, 1)
g4.addEdge(0, 3)
g4.addEdge(3, 4)
print("Yes" if g4.isBC() else "No")

g5 = Graph(3)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 0)
print("Yes" if g5.isBC() else "No")
