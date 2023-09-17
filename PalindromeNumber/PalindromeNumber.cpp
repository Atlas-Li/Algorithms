#include<iostream>
using namespace std;

bool isPalindrome(int x) {
    if (x < 0)  return false;

    long reversed = 0;
    long temp = x;

    while(temp != 0){
        int digit = temp % 10;
        reversed = reversed * 10 + digit;
        temp /= 10;
    }

    return (reversed == x);
}

int main(){
    int x = 121;
    cout << isPalindrome(x) << endl;
    return 0;
}