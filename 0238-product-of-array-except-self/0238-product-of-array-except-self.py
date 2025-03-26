class Solution(object):
    def productExceptSelf(self, nums):
        pref = []
        prod = 1
        for i in range(len(nums)):
            if(i==0):
                pref.append(1)
            else:
                prod = prod*nums[i-1]
                pref.append(prod)
        prod = 1
        suff =[]
        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suff.append(1)
            else:
                prod = prod*nums[i+1]
                suff.append(prod)
        suff.reverse()
        for i in range(len(nums)):
            nums[i]=pref[i]*suff[i]
        return nums

        
        