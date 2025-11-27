class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mpp = {}
        mpp[0]=1
        sum = 0
        cnt = 0

        for num in nums:
            sum+=num
            if sum%k in mpp:
                cnt += mpp[sum%k]
            mpp[sum%k] = mpp.get(sum%k,0) + 1
        return cnt
