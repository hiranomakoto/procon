# abc180 C
# https://atcoder.jp/contests/abc180/tasks/abc180_c
# 約数列挙

n = int(input())

ans = []
bak = []

i = 1
while(i ** 2 < n):
    if n % i == 0:
        ans.append(i)
        if not i ** 2 == n:
            bak.append(n//i)
    i += 1

for i in ans:
    print(i)
for i in bak[::-1]:
    print(i)

