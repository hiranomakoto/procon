S = input()
S_list = []
start = False
buf = ''
for s in S:
    buf += s
    if s.isupper():
        if start:
            S_list.append(buf)
            buf = ''
            start = False
        else:
            start = True

S_list = sorted(S_list, key=lambda s: [c.lower() for c in s])
print(''.join(S_list))
