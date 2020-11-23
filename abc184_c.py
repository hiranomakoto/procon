

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

# 移動しないパターン
if r1 == r2 and c1 == c2:
    print(0)
# 一回の移動で済むパターン
elif (r1-c1) == (r2-c2) or (r1+c1) == (r2+c2) or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
# 斜め2回で行けるパターン
elif (abs(r1-r2) + abs(c1-c2)) % 2 == 0:
    print(2)
# 斜めじゃない移動2回で行けるパターン
elif abs(r1-r2) + abs(c1-c2) <= 6:
    print(2)
# 斜め1回と斜めじゃない1回で行けるパターン
elif abs((r1-c1) - (r2-c2)) <= 3 or abs((r1+c1) - (r2+c2)) <= 3:
    print(2)
else:
    print(3)


