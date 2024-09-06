class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> ch;
        for(int i = 0 ; i < s.size();i++){
            if(s[i]=='\0'){
                continue;
            }
            if(isalnum(s[i])){
                s[i] = tolower(s[i]);
                ch.push_back(s[i]);
            }   
        }
        int start = 0;
        int end = ch.size()-1;
        while(start<end){
            if(ch[start++]!=ch[end--]){
                return false;
            }
        }
        return true;
        
        
    }
};