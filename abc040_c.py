# abc040 c
# https://atcoder.jp/contests/abc040/tasks/abc040_c
# 動的計画法

n = int(input())
a = list(map(int,input().split()))

INF = 2 ** 30
dp = [INF for _ in range(n)]
dp[0] = 0

for i in range(n-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(a[i] - a[i+1]))
    if(i < n-2):
        dp[i+2] = min(dp[i+2], dp[i] + abs(a[i] - a[i+2]))

print(dp[-1])
