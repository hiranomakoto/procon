# ABC E
# https://atcoder.jp/contests/abc183/tasks/abc183_e
# 動的計画法でやったが、どうしても2ケースでTLEする
# 未AC O(H*W)でできていると思うので、いけるはずなのだが。。。


MOD = 10 ** 9 + 7
th = MOD * 1000

h,w = map(int,input().split())

map=['#' * (w+1)]
for _ in range(h):
    map.append('#' + input())

dp = [[0 for _ in range(w+1)] for _ in range(h+1)]

sum_h = [[0 for _ in range(w+1)] for _ in range(h+1)]
sum_v = [[0 for _ in range(w+1)] for _ in range(h+1)]
sum_d = [[0 for _ in range(w+1)] for _ in range(h+1)]

dp[1][1] = 1
sum_h[1][1] = 1
sum_v[1][1] = 1
sum_d[1][1] = 1

for i in range(2,w+1):
    if map[1][i] == '.':
        dp[1][i] = sum_h[1][i-1]
        sum_h[1][i] = sum_h[1][i-1] + dp[1][i]
        sum_v[1][i] = dp[1][i]
        sum_d[1][i] = dp[1][i]
    else:
        break

for i in range(2,h+1):
    if map[i][1] == '.':
        dp[i][1] = sum_v[i-1][1]
        sum_v[i][1] = sum_v[i-1][1] + dp[i][1]
        sum_h[i][1] = dp[i][1]
        sum_d[i][1] = dp[i][1]
    else:
        break

for i in range(2,h+1):
    for j in range(2,w+1):
        if map[i][j] == '#':
            continue
        dp[i][j] = sum_v[i-1][j] + sum_h[i][j-1] + sum_d[i-1][j-1]
        sum_h[i][j] = sum_h[i][j-1] + dp[i][j]
        sum_v[i][j] = sum_v[i-1][j] + dp[i][j]
        sum_d[i][j] = sum_d[i-1][j-1] + dp[i][j]
        if sum_h[i][j] > th:
            sum_h[i][j] %= MOD
            sum_v[i][j] %= MOD
            sum_d[i][j] %= MOD

print(dp[h][w] % MOD)
