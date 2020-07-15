def dfs(start, edge, visited):
    point = set()
    stack = []
    count = 0
    mv = 0
    point.add(start)
    stack.extend(edge[start])
    visited[start] += 1
    while stack:
        start = stack.pop(0)
        if visited[start]:
            mv += 1
            continue
        visited[start] += 1
        point.add(start)
        stack = edge[start] + stack
        mv += 1
    if len(point) == mv + 1:
        return 1, visited
    else:
        return 0, visited


case = 1
while True:
    # data input
    p, e = list(map(int, input().split()))  # 정점, 간선 갯수
    if not p + e:  # 종료조건
        break

    edges = [[] for _ in range(p+1)] # 인접 리스트
    visited = [0 for _ in range(p+1)] # p의 방문여부

    for _ in range(e): # read edges
        t = list(map(int, input().split()))
        edges[t[0]].append(t[1])

    tree = 0
    for x in range(1, p+1):
        if visited[x]:
            continue
        t, visited = dfs(x, edges,  visited=visited)
        tree += t

    if tree == 1:
        print(f"Case {case}: There is one tree.")
    if tree > 1:
        print(f"Case {case}: A forest of {tree} trees.")
    if not tree:
        print(f"Case {case}: No trees.")
    case += 1
