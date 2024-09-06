class Solution {
public:
    bool isPowerOfTwo(int n) {
        long long ans = -1;
        int i = 0;
        while(ans<n){
            ans = pow(2,i);
            i++;
            if(ans==n){
                return true;
            }


        }
        return false;
        
    }
};