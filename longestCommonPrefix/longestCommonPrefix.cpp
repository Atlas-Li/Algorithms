#include<iostream>
#include<vector>
using namespace std;

string longestCommonPrefix(vector<string> &strs){
    string ans = "";
    sort(strs.begin(), strs.end());
        
    int num = strs.size();

    string f = strs[0];
    string l = strs[num-1];

    for (int i=0; i<min(f.size(), l.size()); i++){
        if (f[i] != l[i]) return ans;
        ans += f[i];
    }
    return ans;
}

int main(){
    vector<string> strs = {"flower","flow","flight"};
    cout << longestCommonPrefix(strs) << endl;
    return 0;
}