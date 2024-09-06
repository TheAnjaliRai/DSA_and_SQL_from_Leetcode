class Solution {
public:
    int romanToInt(string s) {
        int res=0;
        unordered_map<char,int> mapp = {
            {'I' , 1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
        };
        for(int i = 0 ; i<s.size() ; i++){
            if(i+1<s.size() && mapp[s[i]]<mapp[s[i+1]]){
                res = res - mapp[s[i]];
            }
            else{
                res = res + mapp[s[i]];
            }
        }
        return res;

        
    }
};