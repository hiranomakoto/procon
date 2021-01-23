# https://atcoder.jp/contests/abc189/tasks/abc189_d
# 動的計画法

n = int(input())
S = []

for _ in range(n):
    s = input()
    S.append(s)

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(n):
    if S[i] == 'AND':
        dp[i+1] = dp[i]
    else:
        dp[i+1] = 2 ** (i+1) + dp[i]

print(dp[n])

