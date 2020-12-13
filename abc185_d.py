# https://atcoder.jp/contests/abc185/tasks/abc185_d
# 連続した白いマスの長さを求めて、その中の最短のものをkと取る
# 各連続した白いマスについて、何度スタンプを押す必要があるかを求めて足し合わせる

n,m = map(int,input().split())
parts = []
if m:
    a = list(map(int,input().split()))
    a.sort()
    prev = 0
    for p in a:
        if p > prev + 1:
            parts.append(p - prev - 1)
        prev = p
    if n > prev:
        parts.append(n - prev)
else:
    a = []
    parts = [n]

ans = 0
stamp = 0

if parts:
    stamp = min(parts)
    for p in parts:
        if p % stamp == 0:
            ans += (p // stamp)
        else:
            ans += (p // stamp + 1)

print(ans)
#print(stamp)
#print(parts)
#print(a)
