class Solution(object):
    def lengthOfLongestSubstring(self, s):
        li=set()
        left = 0
        right = 0
        maxlen = 0
        for right in range(len(s)):
            while s[right] in li:
                li.remove(s[left])
                left+=1
            li.add(s[right])
            maxlen=max(maxlen,right-left+1)
        
        return maxlen

        