# ABC186 D
# https://atcoder.jp/contests/abc186/tasks/abc186_d

n =int(input())
a = list(map(int,input().split()))
a.sort()

basement = 0
for i in range(1,n):
    basement += a[i] - a[0]

ans = basement

for i in range(1,n-1):
    basement = (basement - (a[i] - a[i-1]) * (n - i))
    ans += basement

print(ans)
