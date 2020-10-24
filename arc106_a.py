# arc106 A問題 A - 106
# https://atcoder.jp/contests/arc106/tasks/arc106_a

n = int(input())

count5 = 0
m = 1
flag = False
while(m < n):
    count5 += 1
    m *= 5
    t = n - m
    count3 = 0
    while(t > 0 and t % 3 == 0):
        count3 += 1
        t //= 3
        if t == 1:
            flag = True
            break
    if flag:
        break

if flag:
    print(count3,count5)
else:
    print(-1)
