'''
Dijkstra Algorithm for shortest path
'''

def solve(n, m, edges, source):
    adj = [[] for _ in range(n + 1)]

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    vis = [False] * (n + 1)
    par = [-1] * (n + 1)

    dist[source] = 0

    for _ in range(n):
        u = -1
        mn = INF
        for i in range(1, n + 1):
            if not vis[i] and dist[i] < mn:
                mn = dist[i]
                u = i

        if u == -1:
            break

        vis[u] = True

        for v, w in adj[u]:
            if not vis[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                par[v] = u

    print("Dijkstra Shortest Path Report")
    print(f"Vertices: {n}")
    print(f"Edges: {m}")
    print(f"Source Vertex: {source}")

    print("Shortest Path Table")

    for i in range(1, n + 1):
        if dist[i] == INF:
            print(f"{i}: Distance = INF, Path = None")
        else:
            path = []
            cur = i
            while cur != -1:
                path.append(str(cur))
                cur = par[cur]
            path.reverse()
            print(f"{i}: Distance = {dist[i]}, Path = {' -> '.join(path)}")

    print("Complexity: O(n^2)")
    print("Observation: Dijkstra's algorithm finds shortest paths from the source to all reachable vertices in graphs with positive edge weights.")