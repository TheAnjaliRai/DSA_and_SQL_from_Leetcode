class Solution(object):
    def longestPalindrome(self, s):
        n  = len(s)
        if n==0:
            return ""
        
        start,maxlen = 0,1
        for i in range(n):
            for j in range(2):
                low,high = i,i+j

                while low>=0 and high <n and s[low]==s[high]:
                    curlen = high - low+1
                    if curlen>maxlen:
                        start = low
                        maxlen = curlen
                    low-=1
                    high+=1
        return s[start:start + maxlen]
        