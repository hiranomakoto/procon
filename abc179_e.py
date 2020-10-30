# abc179 E Sequence Sum
# https://atcoder.jp/contests/abc179/tasks/abc179_e
# 剰余をとるので変数が周期的になるパターン

from collections import defaultdict

n,x,m = map(int,input().split())

hist = defaultdict(int)
hist[x] = 1
part_add = [0,x]

i = n
for i in range(2,n+1):
    x = x ** 2 % m
    if hist[x] > 0:
        start = hist[x]
        break
    else:
        hist[x] = i
        part_add.append(part_add[-1] + x)

if i == n:
    print(part_add[-1])
else:
    repetition = (n - start + 1) // (i - start)
    remaining = (n - start + 1) % (i - start)
    ans = (part_add[-1] - part_add[start-1]) * repetition + part_add[start + remaining - 1]
    print(ans)

