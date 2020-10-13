"""
HHKBコンテスト B
https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_b
動的計画法
"""

h,w = map(int,input().split())

map = []
for _ in range(h):
    map.append(input())

dp = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h-1):
    if map[i+1][0] == map[i][0] == '.':
        dp[i+1][0] = dp[i][0] + 1
    else:
        dp[i+1][0] = dp[i][0]

for i in range(w-1):
    if map[0][i+1] == map[0][i] == '.':
        dp[0][i+1] = dp[0][i] + 1
    else:
        dp[0][i+1] = dp[0][i]

for i in range(h-1):
    for j in range(w-1):
        dp[i+1][j+1] += dp[i][j+1] + dp[i+1][j] - dp[i][j]
        if map[i+1][j+1] == '.':
            if map[i][j+1] == '.':
                dp[i+1][j+1] += 1
            if map[i+1][j] == '.':
                dp[i+1][j+1] += 1

print(dp[-1][-1])