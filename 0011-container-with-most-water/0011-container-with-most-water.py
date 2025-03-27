class Solution(object):
    def maxArea(self, height):
        # maxvol = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1 , len(height)):
        #         width = j -i
        #         ht = min(height[i],height[j])
        #         vol = width*ht
        #         maxvol = max(maxvol,vol)
        # return maxvol

        maxvol = 0
        start = 0
        end = len(height)-1
        while(start<end):
            maxvol = max(maxvol,min(height[start],height[end])*(end-start))
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return maxvol





        