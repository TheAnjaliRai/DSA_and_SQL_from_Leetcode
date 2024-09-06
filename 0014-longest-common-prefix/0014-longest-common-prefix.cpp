class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int ans = -1;
        string first = strs[0];
        int n = strs.size();
        string last = strs[n-1];

        int m = min(first.length(),last.length());
        for(int i = 0 ; i <m;i++){
            if(first[i]!=last[i]){
                break;
            }
            else{
                ans++;
            }
            
        }

        string a = "";
        for(int i = 0 ; i <=ans ; i++){
            a.push_back(first[i]);
        }
        return a;
        
    }
};