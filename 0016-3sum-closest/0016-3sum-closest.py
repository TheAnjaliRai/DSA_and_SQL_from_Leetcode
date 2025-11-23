class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        if target == ans:
            return ans
        for i in range(0,len(nums)):
            new_target = target - nums[i]
            start = i+1
            end = len(nums)-1
            while start<end:
                s = nums[start] + nums[end] + nums[i]
                curr_diff = abs(target - s)

                if curr_diff < abs(target - ans):
                    ans = s

                if s <target:
                    start+=1
                elif s > target:
                    end-=1
                else:
                    return s

        return ans

                


        