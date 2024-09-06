int square_of_digit(int n){
    int sum = 0;
    while(n>0){
        int rem = n%10;
        sum = sum + rem*rem;
        n = n/10;
    }
    return sum;
}


class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = square_of_digit(n);
        while(fast!=1 && slow!=fast){
            slow = square_of_digit(slow);
            fast = square_of_digit(square_of_digit(fast));

        }
        if(fast==1){
            return true;
        }
        return false;
    }
    
};