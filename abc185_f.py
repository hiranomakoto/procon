# ABC185 F
# https://atcoder.jp/contests/abc185/tasks/abc185_f
# セグメント木

class segmetTree(object):
    def __init__(self,n,func,NA):
        self.NA = NA
        x = 1
        while(n>x):
            x *= 2
        self.n = x
        self.dat = [self.NA for _ in range(2*x)]
        self.func = func
    
    def update(self,i,x):
        i += (self.n - 1)
        self.dat[i] = x
        while(i > 0):
            # 親を順次更新
            i = (i - 1) // 2
            self.dat[i] = self.func(self.dat[i * 2 + 1], self.dat[i * 2 + 2])
    
    def query_sub(self,a,b,k,l,r):
        if r <= a or b <= l:
            return self.NA
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query_sub(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query_sub(a, b, k * 2 + 2, (l + r) // 2, r)
            return self.func(vl, vr)
    
    def query(self,a,b):
        return self.query_sub(a,b,0,0,self.n)


n,q = map(int,input().split())

st = segmetTree(n,lambda x,y: x ^ y,0)

for i,a in enumerate(map(int,input().split())):
    st.update(i,a)

for _ in range(q):
    t,x,y = map(int,input().split())
    if t == 1:
        st.update(x-1, st.query(x-1,x) ^ y)
    else:
        print(st.query(x-1,y))
