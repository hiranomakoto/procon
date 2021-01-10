# https://atcoder.jp/contests/abc188/tasks/abc188_c
# 完全二分木

n = 2 ** int(input())

A = list(map(int,input().split()))

B = {}
t = [0 for _ in range(n*2)]

for i,a in enumerate(A):
    B[a] = i+1
    t[i+n-1] = a

for k in range(n-2,-1,-1):
    t[k] = max(t[2*k+1],t[2*k+2])

print(B[min(t[1],t[2])])
