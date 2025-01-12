"""
https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
ダイクストラ法練習問題

"""

import heapq

def dijkstra(n, graph, start):
    # この実装ではdistの初期値としてfloat('inf')を使っている
    # 訪問済みか否かを判定するための別のint変数を使う方法もある
    # この実装のほうがすっきりはするが、どちらが良いかはよくわからない
    dist = [float('inf')]*n
    dist[start] = 0
    hq = [(0, start)]
    heapq.heapify(hq)
    while hq:
        d, v = heapq.heappop(hq)
        if dist[v] < d:
            continue
        for u, cost in graph[v]:
            if dist[u] > dist[v] + cost:
                dist[u] = dist[v] + cost
                heapq.heappush(hq, (dist[u], u))
    return dist

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

print(dijkstra(n, graph, 0)[n-1])

