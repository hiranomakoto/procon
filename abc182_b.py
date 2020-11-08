# ABC182 B
# https://atcoder.jp/contests/abc182/tasks/abc182_b
# 共通の因数の最大値

n = int(input())
a = map(int,input().split())

count = [0 for _ in range(1001)]
for i in a:
    for j in range(1,i+1):
        if j * j > i:
            break
        if i % j == 0:
            count[j] += 1
            if not j * j == i:
                count[i//j] += 1

ans = 2
for i in range(2,1000):
    if count[ans] < count[i]:
        ans = i
print(ans)
