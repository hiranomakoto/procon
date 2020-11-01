# abc181 C
# https://atcoder.jp/contests/abc181/tasks/abc181_c
# 任意の3点a,b,cを選んでa->bとa->cの勾配が同じであることか判定すればよい
# x軸かy軸に平行なケースだけケアする必要がある

import sys

n = int(input())
x = []
y = []
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (x[i] == x[j]) or (x[i] == x[k]):
                if x[i] == x[j] == x[k]:
                    print('Yes')
                    sys.exit()
                else:
                    continue
            if (y[i] - y[j])*(x[i] - x[k]) == (y[i] - y[k])*(x[i] - x[j]):
                print('Yes')
                sys.exit()

print('No')
