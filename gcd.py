# 最小公倍数

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b, r)