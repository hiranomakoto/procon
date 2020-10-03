# TDPC A
# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
# 動的計画法

n = int(input())
p = list(map(int,input().split()))

dp = [[0 for _ in range(10100)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(10100):
        if dp[i][j] > 0:
            dp[i+1][j] = 1
            dp[i+1][j+p[i]] = 1

print(sum(dp[n]))
