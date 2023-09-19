#include<iostream>
#include<vector>
using namespace std;

int removeElement(vector<int>& nums, int val) {
    if (nums.size() == 0) return 0;

    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != val) {
            nums[count] = nums[i];
            count++;
        }
    }
    return count;
}


int main(){
    vector<int> nums = {3,2,2,3};
    int val = 3;
    int result = removeElement(nums, val);
    cout << result << endl;

    for (int i = 0; i < result; i++) {
        cout << nums[i] << " ";
    }
    return 0;
}