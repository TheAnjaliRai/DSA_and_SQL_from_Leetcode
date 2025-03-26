class Solution(object):
    def findKthLargest(self, nums, k):
        nums = sorted(nums , reverse = True)
        # cnt = 1
        # curr = nums[0]
        
        # for i in range(1,len(nums)):
        #     if(k==cnt):
        #         return curr
        #     if(curr!=nums[i]):
        #         curr = nums[i]
        #         cnt+=1
            
        return nums[k-1]