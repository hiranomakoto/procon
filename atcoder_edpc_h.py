# atcoder edpc H問題
# https://atcoder.jp/contests/dp/tasks/dp_h
# 動的計画法　数え上げ


MOD = 10**9 + 7
h,w = map(int,input().split())

field = []
for _ in range(h):
    field.append(input())

dp = [[0 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1

for i in range(h-1):
    if field[i+1][0] == '.':
        dp[i+1][0] = 1
    else:
        break

for i in range(w-1):
    if field[0][i+1] == '.':
        dp[0][i+1] = 1
    else:
        break

for i in range(h-1):
    for j in range(w-1):
        if field[i+1][j+1] == '.':
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j]) % MOD

print(dp[h-1][w-1])
