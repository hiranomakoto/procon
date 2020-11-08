# ABC182 C
# https://atcoder.jp/contests/abc182/tasks/abc182_c
# 各桁の合計が3の倍数であれば元の数は3の倍数、の問題

n = int(input())

dig = []
while(n):
    dig.append(n%10)
    n //= 10

a = sum(dig) % 3
if a == 0:
    print(0)
else:
    amari = [0,0,0]
    for i in dig:
        b = i % 3
        amari[b] += 1
    if amari[a] > 0 and len(dig) > 1:
        print(1)
    elif amari[a*2 % 3] > 1 and len(dig) > 2:
        print(2)
    else:
        print(-1)
