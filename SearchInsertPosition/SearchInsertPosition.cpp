#include<iostream>
#include<vector>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int n = nums.size();

    int start = 0;
    int end = n - 1;

    while(start <= end){
        int mid = start + (end - start) / 2;

        if (nums[mid] == target) return mid;
        else if(nums[mid] < target) start = mid + 1;
        else end = mid - 1;
    }
    return start;
}

int main(){
    vector<int> nums = {1,3,5,6};
    int target = 5;
    cout << searchInsert(nums, target) << endl;
    return 0;
}