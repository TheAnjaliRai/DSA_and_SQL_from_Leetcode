class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0;
        bool lead = true;
        vector<int> ans;
        int n = digits.size();
        digits[n-1]+=1;
        for(int i = n-1 ; i>=0 ;i--){
            digits[i] += carry;
            if(digits[i]>9){
                ans.insert(ans.begin(),0);
                carry = 1;
            }
            else{
                ans.insert(ans.begin(),digits[i]);
                carry = 0;
            }
        
            
        }
        if(carry==1){
            ans.insert(ans.begin(),1);
        }
        return ans;
    }
};