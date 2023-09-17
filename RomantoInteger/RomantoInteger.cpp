#include<iostream>
#include <unordered_map>
using namespace std;

int romanToInt(string s) {
    unordered_map<char, int> sv;
    sv['I'] = 1;
    sv['V'] = 5;
    sv['X'] = 10;
    sv['L'] = 50;
    sv['C'] = 100;
    sv['D'] = 500;
    sv['M'] = 1000;

    int ans = 0;

    for (int i=0; i<s.length(); i++){
        if (sv[s[i]] < sv[s[i+1]]) ans -= sv[s[i]];
        else    ans += sv[s[i]];
    }
    return ans;
}

int main(){
    string s = "MCMXCIV";   // 1994
    cout << romanToInt(s) << endl;
    return 0;
}