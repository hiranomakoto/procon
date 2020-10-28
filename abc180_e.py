# ABC E問題　巡回セールスマン問題
# https://atcoder.jp/contests/abc180/tasks/abc180_e
# 巡回セールスマン
# https://tic40.hatenablog.com/entry/2020/10/18/110837
# の答えの写経

INF = 10 ** 12

n = int(input())

x = []
y = []
z = []

for _ in range(n):
    a,b,c = map(int,input().split())
    x.append(a)
    y.append(b)
    z.append(c)

dp = [[ INF for _ in range(n)] for _ in range(1<<n)]

cost = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a = abs(x[j] - x[i])
        b = abs(y[j] - y[i])
        c = max(0,z[j] - z[i])
        cost[i][j] = a+b+c

for i in range(1,n):
    dp[1<<i][i] = cost[0][i]

for i in range(1<<n):
    for j in range(n):
        if i >> j & 1 == 0:
            continue
        for k in range(n):
            if i >> k & 1:
                continue
            dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j] + cost[j][k])

print(dp[(1<<n)-1][0])
