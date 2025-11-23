class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        target = 0
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            first = nums[i]
            new_target = target - first
            start = i+1
            end = len(nums)-1
            while start < end:
                sum = nums[start] + nums[end]
                if sum==new_target:
                    res.append([first,nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                elif sum<new_target:
                    start+=1
                else:
                    end-=1
            
        return res


                