class Solution {
public:
    string addBinary(string a, string b) {
        string s;
        int n1=a.size()-1;
        int n2 = b.size()-1;
        int chara;
        int charb;
        int carry = 0;
        while(carry || n1>=0||n2>=0){
            if(n1<0){
                chara = 0;
            }
            else{
                chara = a[n1] -'0';
            }

            if(n2<0){
                charb = 0; 

            }
            else{
                charb = b[n2]-'0';
            }
            
            
            if(chara+charb+carry==0){
                s.insert(s.begin(),'0');
                carry = 0;
                n1--;
                n2--;

            }
            else if(chara+charb+carry==1){
                s.insert(s.begin(),'1');
                carry = 0;
                n1--;
                n2--;


            }
            else if(chara+charb+carry==2){
                s.insert(s.begin(),'0');
                carry = 1;
                n1--;
                n2--;

            }
            else{
                s.insert(s.begin(),'1');
                carry = 1;
                n1--;
                n2--;

            }

        }
        return s;

    }
};