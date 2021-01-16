# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_a
# 数列を前から舐めてそれぞれの最大値を更新していく

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = [1 for _ in range(n)]
c[0] = a[0] * b[0]
a_max = 0
b_max = 0

for i in range(1,n):
    if a[i] > a[a_max]:
        c[i] = max(c[i-1], a[i] * b[i])
        a_max = i
    else:
        c[i] = max(c[i-1], a[a_max] * b[i])
        if c[i-1] < c[i]:
            b_max = i

for c_i in c:
    print(c_i)
