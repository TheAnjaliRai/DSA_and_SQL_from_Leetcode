class Solution(object):
    def isPalindrome(self, s):
        line=""
        for str in s:
            if (str>='a' and str<='z') or (str>='A' and str<='Z') or (str>='0' and str<='9'):
                line=line+lower(str)
        start = 0
        end = len(line)-1
        while(start<end):
            if line[start]!=line[end]:
                return False
            start+=1
            end-=1
        return True


        