# https://atcoder.jp/contests/abc037/tasks/abc037_d
# トポロジカルソートしての動的計画法

h,w = map(int,input().split())
MOD = 10 ** 9 + 7

# グラフの周囲を0で囲む
edge = [0 for _ in range(w+2)]
field = [edge]
for _ in range(h):
    a = list(map(int,input().split()))
    field.append([0] + a + [0])
field.append(edge)

dp = [[1 for _ in range(w+2)] for _ in range(h+2)]
G = [[[] for _ in range(w+2)] for _ in range(h+2)]
deg = [[0 for _ in range(w+2)] for _ in range(h+2)]

for x in range(1,w+1):
    for y in range(1,h+1):
        next_hop = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        for na in [n for n in next_hop if field[n[1]][n[0]] > field[y][x]]:
            G[y][x].append(na)
            deg[na[1]][na[0]] += 1

queue = []
ans = 0

for x in range(1,w+1):
    for y in range(1,h+1):
        if deg[y][x] == 0:
            queue.append((x,y))
            ans += 1

while(queue):
    x,y = queue.pop()
    for nx,ny in G[y][x]:
        deg[ny][nx] -= 1
        dp[ny][nx] += dp[y][x]
        dp[ny][nx] %= MOD
        if deg[ny][nx] == 0:
            queue.append((nx,ny))
            ans += dp[ny][nx]
print(ans % MOD)

"""
ans = 0
for x in range(1,w+1):
    for y in range(1,h+1):
        ans += dp[y][x]
print(ans)

for p in dp:
    print(p)
"""