class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans;
        map<int,int> mapp;
        int n = nums.size();
        for(int i = 0;i <=n;i++){
            mapp[i]=0;
        }
        for(int i = 0 ; i < n ; i++){
            mapp[nums[i]]=1;
        }
        for(int i = 0 ; i<=n;i++){
            if(mapp[i]==0){
                ans = i;
                break;
                
            }
        }
        return ans;
        
        




        
        
    }
};