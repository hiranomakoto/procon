# ABC182 D
# https://atcoder.jp/contests/abc182/tasks/abc182_d
# 部分和の考え方を使って解く

n = int(input())
a = list(map(int,input().split()))

part_add = []
s = 0
for i in a:
    s += i
    part_add.append(s)

part_max = []
s = a[0]
for i in range(n):
    s = max(s,part_add[i])
    part_max.append(s)

base_pos = [0]
s = 0
for i in part_add:
    s += i
    base_pos.append(s)

ans = 0
for b,p in zip(base_pos,part_max):
    ans = max(ans,b+p)

print(ans)
