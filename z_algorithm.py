# 下記qiita記事からコピー
# https://qiita.com/t_fuki/items/e682238dda6ad832ce05 

# 下記解説記事はわかりやすい
# https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05

def z_algorithm(s):
    z = [0]*len(s)
    z[0] = len(s)
    l = r = 0
    for i in range(1,len(s)):
        if z[i-l] < r-i:
            z[i] = z[i-l]
        else:
            r = max(r,i)
            while r < len(s) and s[r] == s[r-i]:
                r += 1
            z[i] = r-i
            l = i
    return z
