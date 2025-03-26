class Solution(object):
    def trap(self, height):
        if not height or len(height) < 3:  # Ensure there are at least 3 bars to trap water
            return 0
        left = []
        right = []
        curr = 0
        for i in range(len(height)):
            curr = max(curr,height[i])
            left.append(curr)
        curr = 0
        for i in range(len(height)-1 , -1,-1):
            curr = max(curr,height[i])
            right.append(curr)

        right.reverse()
        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]

            
        return total



        