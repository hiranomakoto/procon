# abc181 D
# https://atcoder.jp/contests/abc181/tasks/abc181_d
# 8の倍数を判定する問題
# 1000が8の倍数なので、下3桁だけの議論にすればよい

import sys

s = input()
num_dict = {}

for t in s:
    num = int(t)
    if num in num_dict.keys():
        num_dict[num] += 1
    else:
        num_dict[num] = 1

candidates = []
for i in num_dict.keys():
    if num_dict[i] > 2:
        candidates.append(i)
        candidates.append(i)
        candidates.append(i)
    elif num_dict[i] == 2:
        candidates.append(i)
        candidates.append(i)
    else:
        candidates.append(i)

#print(num_dict)
#print(candidates)

n = len(candidates)
if  n == 1:
    if candidates[0] == 8:
        print('Yes')
    else:
        print('No')
elif n == 2:
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (candidates[i] * 10 + candidates[j]) % 8 == 0:
                print('Yes')
                sys.exit()
    print('No')
else:
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if j == k or i == k:
                    continue
                if (candidates[i] * 100 + candidates[j] * 10 + candidates[k]) % 8 == 0:
                    print('Yes')
                    sys.exit()
    print('No')
