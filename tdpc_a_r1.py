# TDPC A 別解
# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
# 動的計画法
# 辞書にしたら検索処理がない分大幅に早くなるかと思ったが、
# そこまで変わらなかった

n = int(input())
p = list(map(int,input().split()))

dp = {}
dp[0] = 1

for i in range(n):
    keys = list(dp.keys())[::]
    for j in keys:
        dp[j+p[i]] = 1

print(len(dp.keys()))

