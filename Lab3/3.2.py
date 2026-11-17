'''
Graph representation using adjacency list and adjacency matrix
'''

def solve(n, m, edges):
    mat = [[0] * (n + 1) for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]

    for u, v in edges:
        mat[u][v] = 1
        mat[v][u] = 1
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        adj[i].sort()

    print("Graph Representation Report")
    print(f"Vertices: {n}")
    print(f"Edges: {m}")

    print("Adjacency Matrix")
    for i in range(1, n + 1):
        print(*mat[i][1:])

    print("Adjacency List")
    for i in range(1, n + 1):
        if adj[i]:
            print(f"{i}:", *adj[i])
        else:
            print(f"{i}: None")

    matrix_space = n * n
    list_space = n + 2 * m

    print("Space Comparison")
    print(f"Adjacency Matrix Space Units: {matrix_space}")
    print(f"Adjacency List Space Units: {list_space}")

    max_edges = n * (n - 1) // 2

    if m <= max_edges / 2:
        graph_type = "Sparse"
        recommendation = "Adjacency List"
    else:
        graph_type = "Dense"
        recommendation = "Adjacency Matrix"

    print(f"Graph Type: {graph_type}")
    print(f"Recommended Representation: {recommendation}")

    if recommendation == "Adjacency List":
        print("Observation: Adjacency List uses less space for sparse graphs.")
    else:
        print("Observation: Adjacency Matrix provides fast edge lookup for dense graphs.")