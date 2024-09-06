class Solution {
public:
    bool isPowerOfThree(int n) {
        int i = 0;
        long long ans = -1;
        while(ans<n){
            ans = pow(3,i);
            if(ans==n){
                return true;
            }
            i++;
        }
        return false;
        
    }
};