class Solution {
public:
    int arrangeCoins(int n) {
        bool comp = true;
        int step = 0;
        int need = 1;
        while(comp){
            if(n>=need){
                n = n - need;
                need++;
                step++;
            }
            else{
                return step;
            }
        }
        return step;
        
    }
};