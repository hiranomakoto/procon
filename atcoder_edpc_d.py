# EDPC D
# https://atcoder.jp/contests/dp/tasks/dp_d
# ナップサック問題

n,tw = map(int,input().split())
w = []
v = []
for _ in range(n):
    wi,vi = map(int,input().split())
    w.append(wi)
    v.append(vi)

dp = [[0 for _ in range(tw + 10)] for _ in range(n + 1)]

for i in range(n):
    for wsum in range(tw + 1):
        if w[i] <= wsum:
            dp[i+1][wsum] = max(dp[i+1][wsum],dp[i][wsum - w[i]] + v[i])
        dp[i+1][wsum] = max(dp[i+1][wsum],dp[i][wsum])

print(dp[n][tw])
