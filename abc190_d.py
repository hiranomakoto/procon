# https://atcoder.jp/contests/abc190/tasks/abc190_d
# 約数列挙して、それぞれの約数の偶奇判定をする

n = int(input())

if n == 1:
    print(2)
    exit()

ans = 0
for i in range(1,n):
    if i * i > n:
        break
    if n % i == 0:
        if i * i == n and i % 2 == 1:
            ans += 2
        else:
            if i % 2 == 1:
                ans += 2
            if (n // i) % 2 == 1:
                ans += 2
        
print(ans)
