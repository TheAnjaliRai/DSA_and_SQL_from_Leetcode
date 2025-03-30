class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        result = []
        for i in range(n):
            for j in range(2):
                slow,high =i,i+j
                while(slow>=0 and high<n and s[slow]==s[high]):
                    result.append(s[slow:high+1])
                    slow-=1
                    high+=1
        return len(result)
        