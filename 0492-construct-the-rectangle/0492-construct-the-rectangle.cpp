class Solution {
public:
    vector<int> constructRectangle(int area) {

        int fact1 = INT_MAX;
        int fact2 = INT_MIN;
        int diff = INT_MAX;
        for(int i = 1 ; i <= area/2 ; i++){
            if(area%i==0){
                int j = area/i;
                if(diff>abs(i-j)){
                    fact1 = i;
                    fact2 = j;
                    diff = abs(i-j);
                }
                
            }
        }
        vector<int> ans;
        if(area==1){
            ans.push_back(1);
            ans.push_back(1);
            return ans;
        }
        ans.push_back(fact2);
        ans.push_back(fact1);
        return ans;
        
    }
};