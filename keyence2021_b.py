# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b
# これといったアルゴリズムはない

n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

ans = 0
base = 0
boxs = [-1 for _ in range(k)]
preb = -1

for i in a:
    if i > preb:
        b = 0
    if i == boxs[b] + 1:
        boxs[b] = i
        b = (b+1) % k
        ans += 1
    preb = i
    #print(ans,i)

print(ans)
