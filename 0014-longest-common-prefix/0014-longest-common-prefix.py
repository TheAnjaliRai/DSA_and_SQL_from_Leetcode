class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        ans = ''
        a = strs[0]
        b = strs[-1]
        for i in range(len(a)):
            if a[i]==b[i]:
                ans+=a[i]
            else:
                break
        return ans
        
        