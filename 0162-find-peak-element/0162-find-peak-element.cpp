class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        long size = nums.size();
        long long i;
        for(i = 0 ; i < size ; i++){
            if((i==0 || nums[i]>nums[i-1] )&&(i==size-1||nums[i+1]<nums[i])){
                return i;
            }
        }
        return -1;
        
    }
};