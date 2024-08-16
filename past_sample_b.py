n = int(input())
a  = [int(input()) for _ in range(n)]

pre = a[0]
for a_ in a[1:]:
    if pre == a_:
        print('stay')
    elif pre > a_:
        print(f'down {pre - a_}')
    else:
        print(f'up {a_ - pre}')
    pre = a_

