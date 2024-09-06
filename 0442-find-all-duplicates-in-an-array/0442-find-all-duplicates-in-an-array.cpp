class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = nums.size();
        int element = *max_element(nums.begin(),nums.end());
        vector<int> ans_vec(element+1 ,0 );
        for(int i = 0 ; i <n ; i++){
            ans_vec[nums[i]]++;
        }
        vector<int> ans;
        int index = 0;
        for (int i = 0; i <= element; i++) {
            if (ans_vec[i] == 2) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};