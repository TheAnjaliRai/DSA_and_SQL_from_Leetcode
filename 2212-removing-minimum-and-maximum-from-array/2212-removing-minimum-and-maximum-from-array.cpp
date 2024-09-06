class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int mini = 0;
        int maxi = 0;
        int size = nums.size();
        for(int i = 1 ; i < size ; i++){
            if(nums[i]>nums[maxi]){
                maxi = i;
                
            }
            if(nums[i]<nums[mini]){
                mini = i;

            }
        }
        cout << mini << " "<<maxi;

        int slow = min(maxi , mini);
        int fast = max(maxi , mini);

        int ans = min(max(slow+1,fast+1), min(slow + 1 + size - fast,max(size-slow,size-fast)));
        return ans;
        
    }
};