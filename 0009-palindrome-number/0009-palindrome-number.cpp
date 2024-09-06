class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int y = x;
        long pal = 0;
        while(x>0){
            int rem = x%10;
            pal = pal*10 + rem; 
            x = x/10;
        }
        if(pal==y){
            return true;
        }
        return false;
        
    
    }
};