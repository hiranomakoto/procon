"""
HHKBコンテスト C
https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c
"""

n = int(input())
inp = list(map(int,input().split()))
ps = [0 for _ in range(200001)]
l = []
ans = 0
for p in inp:
    ps[p] += 1
    for i in range(ans,200001):
        if ps[i] == 0:
            ans = i
            l.append(i)
            break

for ans in l:
    print(ans)