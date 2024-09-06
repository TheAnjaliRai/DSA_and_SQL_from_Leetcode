class Solution {
public:
    int reverse(int x) {
        
        
        long long num = 0;
        
        int y = x;
        while(y!=0){
        int last_digit = y%10;
        num = num*10 + last_digit;
        if(num<-1*pow(2,31)||num >pow(2,31)-1){
        return 0;}
        y = y/10;
        }
        return static_cast<int>(num);
        
        
        
        
    }
};