# ARC B
# https://atcoder.jp/contests/arc108/tasks/arc108_b
# 文字列操作

n = int(input())
s = '_' + input() + '_'
fox = 'fox'
index = 0
i=0
while(i < n+1):
    if s[i] == fox[index]:
        index += 1
        i += 1
        if index == 3:
            s = s[0:i-3] + s[i:]
            n -= 3
            i = max(0,i-5)
            index = 0
    elif s[i] == fox[0]:
        index = 1
        i += 1
    else:
        index = 0
        i += 1

print(len(s)-2)
