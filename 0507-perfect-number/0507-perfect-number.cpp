class Solution {
public:
    bool checkPerfectNumber(int num) {
        int fact_sum = 0;
        for(int i = 1 ; i<=num/2 ; i++){
            if(num%i==0){
                fact_sum+=i;
            }

        }
        if(fact_sum==num){
            return true;
        }
        else{
            return false;
        }
        
    }
};