#include<iostream>
#include<string>
using namespace std;

int lengthOfLastWord(string s) {
	int s_len = 0;
	bool flag = false;

	for (int i=s.length()-1; i>=0; i--){
		if ((s[i]>='a' && s[i]<='z') ||(s[i]>='A' && s[i]<='Z')){
			flag = true;
			s_len += 1;
		}
		else{
			if(flag == true)    return s_len;
		}
	}
	return s_len;
}

int main(){
	string s = "Hello World ";
	cout << lengthOfLastWord(s) << endl;
	return 0;
}