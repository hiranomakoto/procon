# arc109 C
# https://atcoder.jp/contests/arc109/tasks/arc109_c
# 解説を見ての実装
# 文字列sが偶数長の方がわかりやすいので最初に*2する
# 一周した後は繰り返しなのでまじめに2^kの文字列を考える必要はない

n,k = map(int,input().split())
s = input()
s *= 2
n *= 2

# じゃんけんの勝ち手を返す
jk = {'R':0, 'P':1, 'S':2}
def judge(a,b):
    j = (jk[a] - jk[b]) % 3
    if j == 1:
        return a
    else:
        return b

for _ in range(k):
    # 隣同士でじゃんけんして勝った手を並べる
    l = len(s)
    s = [judge(s[i%l],s[(i+1)%l]) for i in range(0,n,2)]

# k回繰り返した後で先頭の手が優勝した手
print(s[0])
