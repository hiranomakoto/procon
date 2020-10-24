# ARC106 B問題
# https://atcoder.jp/contests/arc106/tasks/arc106_b
# UnionFind木

class UnionFind:
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0]*(n+1)

    # ノードxのrootノードを見つける
    def findRoot(self, x):
        if(self.root[x] < 0): # 根
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.findRoot(x)
        y = self.findRoot(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    # ノードxが属する木のサイズを返す
    def count(self, x):
        return -self.root[self.findRoot(x)]

n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

t = UnionFind(n)

for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    t.unite(a,b)

# 連結成分ごとにまとめる
group = [[] for _ in range(n)]
for i in range(n):
    group[t.findRoot(i)].append(i)

# 各連結成分で、部分列がAとB等しいなら、Yesとなる
flag = True
for i in group:
    if i:
        if not sum([A[a] for a in i]) == sum([B[a] for a in i]):
            flag = False
            break
if flag:
    print('Yes')
else:
    print('No')
