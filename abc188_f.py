# https://atcoder.jp/contests/abc188/tasks/abc188_f
# 公式解説の実装（メモ化再帰）

X,Y = map(int,input().split())

memo = {}
memo[1] = abs(X-1)

def solve(y):
    if y in memo.keys():
        return memo[y]
    if y % 2 == 1:
        memo[y] = min(abs(X-y), solve((y+1)//2) + 2, solve((y-1)//2) + 2)
        return memo[y]
    else:
        memo[y] = min(abs(X-y), solve(y // 2) + 1)
        return memo[y]

print(solve(Y))
