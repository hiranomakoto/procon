# https://atcoder.jp/contests/arc110/tasks/arc110_a
# 最小公倍数を求める問題

import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())

print(lcm_list(list(range(2,n+1)))+1)
