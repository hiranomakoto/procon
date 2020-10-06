# atcoder 第10回日本情報オリンピック予選 D
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
# 動的計画法

n = int(input())
a = list(map(int,input().split()))

"""
第一index番目の数字まで計算した時、第二indexの数字になるパターン数と定義
途中を含めて計算結果はすべて0-20の範囲
"""
dp = [[0 for _ in range(21)] for _ in range(n)]

dp[1][a[0]] = 1

for i in range(2,n):
    for num in range(21):
        if dp[i-1][num] > 0:
            if num + a[i-1] <= 20:
                dp[i][num + a[i-1]] += dp[i-1][num]
            if num - a[i-1] >= 0:
                dp[i][num - a[i-1]] += dp[i-1][num]

def printdp(dp):
    for p in dp:
        print(p)
    return 0

#printdp(dp)

print(dp[n-1][a[-1]])
