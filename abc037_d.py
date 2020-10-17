# https://atcoder.jp/contests/abc037/tasks/abc037_d
# メモ化再帰だが、pythonの再帰はメモリ喰う＋遅いため、TLE/MLE/REになる
# WAにはならなかったので、おそらく理屈はあっているはず
# トポロジカルソートで実施が必要 => abc037_d_r1.py

h,w = map(int,input().split())

# グラフの周囲を0で囲む
edge = [0 for _ in range(w+2)]
G = [edge]
for _ in range(h):
    a = list(map(int,input().split()))
    G.append([0] + a + [0])
G.append(edge)

dp = [[1 for _ in range(w+2)] for _ in range(h+2)]

def rec(x,y):
    if dp[x][y] > 1:
        return dp[x][y]
    
    value = 1
    next_hop = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for na in [n for n in next_hop if G[n[0]][n[1]] > G[x][y]]:
        value += rec(*na)
    dp[x][y] = value
    return value

# for p in G:
#     print(p)

for y in range(1,w+1):
    for x in range(1,h+1):
        rec(x,y)

# for p in dp:
#     print(p)

MOD = 10 ** 9 + 7
ans = 0
for y in range(1,w+1):
    for x in range(1,h+1):
        ans += dp[x][y]

print(ans)
