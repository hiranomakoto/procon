# https://atcoder.jp/contests/arc110/tasks/arc110_b
# 文字列Tが110の連続で表せるかどうかを判定（O(n)）したら
# 10 ^ 10の中にどれだけあるかはO(1)で求まる

n = int(input())
s = input()

def judgement(n,s):
    if n == 1:
        return True
    elif n == 2:
        if s == '00':
            return False
        else:
            return True
    elif n == 3:
        if s == '110' or s == '101' or s == '011':
            return True
        else:
            return False

    elem = '110'
    p = s[:3]
    if p == '110':
        start = 3
    elif p == '101':
        start = 2
    elif p == '011':
        start = 1
    else:
        return False
    
    for i,c in enumerate(s[start:]):
        if not c == elem[i%3]:
            return False
    return True


def calc(n,s):
    if n == 1:
        if s == '1':
            return 2 * 10 ** 10
        else:
            return 10 ** 10
    if n == 2:
        if s == '11' or s == '10':
            return 10 ** 10
        else:
            return 10 ** 10 - 1
    if n == 3:
        if s == '110':
            return 10 ** 10
        else:
            return 10 ** 10 - 1
    p = s[:3]
    if p == '110':
        if n % 3:
            return 10 ** 10 - n // 3
        else:
            return 10 ** 10 - n // 3 + 1
    if p == '101':
        return 10 ** 10 - n // 3
    if p == '011':
        if n % 3 == 2:
            return 10 ** 10 - n // 3 - 1
        else:
            return 10 ** 10 - n // 3

if judgement(n,s):
    print(calc(n,s))
else:
    print(0)
