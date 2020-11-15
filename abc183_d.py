# ABC D
# https://atcoder.jp/contests/abc183/tasks/abc183_d

lim = 2 * 10 ** 5 + 1

n,w = map(int,input().split())

schedule = [0 for _ in range(lim)]

for i in range(n):
    s,t,p = map(int,input().split())
    schedule[s] += p
    schedule[t] -= p

maxi = 0
q = 0
for i in range(lim):
    q += schedule[i]
    maxi = max(maxi,q)

if maxi <= w:
    print('Yes')
else:
    print('No')
