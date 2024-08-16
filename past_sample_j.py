INF = 50 * 50 * 100000 + 1
h,w = map(int,input().split())

A = [[INF for _ in range(w+2)]]
for i in range(h):
    a = list(map(int,input().split()))
    A.append([INF] + a + [INF])
A.append([INF for j in range(w+2)])

cost = [[INF for j in range(w)] for i in range(h)]
fixed = [[False for j in range(w)] for i in range(h)]
fixed[h][1] = True




