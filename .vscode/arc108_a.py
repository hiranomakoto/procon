# ARC 108 A
# https://atcoder.jp/contests/arc108/tasks/arc108_a
# 約数全捜査はsqrt(p)までで十分


s,p = map(int,input().split())

flag = False
for i in range(1,p+1):
    if p % i == 0:
        j = p // i
        if i + j == s:
            flag = True
            break
    if i * i > p:
        break

if flag:
    print('Yes')
else:
    print('No')

