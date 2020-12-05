# 解説の写経

#include <iostream>
#include <string>
#include <vector>
#define rep(X, Y) for (int(X) = 0; (X) < (int)(Y); ++(X))

using namespace std;

int main(void){
    char win[222][222];
    win['R']['R'] = win['R']['S'] = win['S']['R'] = 'R';
    win['S']['S'] = win['S']['P'] = win['P']['S'] = 'S';
    win['P']['P'] = win['P']['R'] = win['R']['P'] = 'P';
    
    int n,k;
    string s;

    cin >> n >> k >> s;

    while(k--){
        const auto t = s + s;
        rep(i,n) s[i] = win[t[i*2]][t[i*2+1]];
        
    }
    cout << s[0] << endl;
}
