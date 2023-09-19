#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool isValid(string s){
    stack<char> st;

    for (char &c : s){
        if (c == '(' || c == '{' || c == '['){
            st.push(c);
        }
        else{
            if (
                st.empty() ||
                (c == ')' && st.top() != '(') ||
                (c == ']' && st.top() != '[') ||
                (c == '}' && st.top() != '{')                 
            )
            {
                return false;
            }
            else{
                st.pop();
            }
        }
    }
    return st.empty();
}

int main(){
    string s = "()[]{}";
    cout << isValid(s) << endl;
    return 0;
}