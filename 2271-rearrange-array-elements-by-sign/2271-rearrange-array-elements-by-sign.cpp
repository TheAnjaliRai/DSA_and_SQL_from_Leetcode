class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> neg;
        vector<int> pos;
        for(int i = 0 ; i<n;i++){
            if(nums[i]>=0){
                pos.push_back(nums[i]);
            }
            else{
                neg.push_back(nums[i]);
            }
        }
        
        vector<int> ans(n);
        int pos_start = 0;
        int neg_start = 0;
        for(int i = 0 ;i <n ; i++){
            if(i%2==0){
                ans[i]=pos[pos_start];
                pos_start++;
            }
            else{
                ans[i]=neg[neg_start];
                neg_start++;
            }
        }

        return ans;

        
        
    }
};