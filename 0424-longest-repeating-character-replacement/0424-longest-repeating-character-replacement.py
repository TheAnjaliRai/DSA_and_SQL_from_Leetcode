class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        char_feq = {}
        max_cnt = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in char_feq:
                char_feq[s[right]]+=1

            else:
                char_feq[s[right]]=1
                
            max_cnt = max(max_cnt , char_feq[s[right]])

            while (right-left+1)-max_cnt >k:
                char_feq[s[left]]-=1
                left+=1
            max_len = max(max_len , right-left+1)
        return max_len

            

        