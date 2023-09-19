#include<iostream>
#include<vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    
    int count = 1;
    for (int i = 1; i < nums.size(); i++;){
        if (nums[i] != nums[i-1]){
            nums[count] = nums[i];
            count++;
        }
    }
    return count;
}


int main(){
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    int count = removeDuplicates(nums);
    cout << count << endl;


    for (int i = 0; i < count; i++){
        cout << nums[i] << " ";
    }
    return 0;
}