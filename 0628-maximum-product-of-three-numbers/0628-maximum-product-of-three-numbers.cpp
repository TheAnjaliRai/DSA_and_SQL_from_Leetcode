class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        if(nums.size()==1){
            return nums[0];
        }
        if(nums.size()==2){
            return nums[0]*nums[1];
        }
        sort(nums.begin(),nums.end());
        int i = nums.size();
        int prod1 = nums[0]*nums[1]*nums[2];
        int prod2 = nums[i-1]*nums[i-2]*nums[i-3];
        int prod3 = nums[0]*nums[1]*nums[i-1];
        return max(max(prod1,prod2),prod3);
    }
};