class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        first = 0
        second = 0
        ans = []
        nums1.sort()
        nums2.sort()
        while first < len(nums1) and second <len(nums2):
            if nums1[first]==nums2[second]:
                ans.append(nums1[first])
                first+=1
                second+=1
            elif nums1[first]<nums2[second]:
                first+=1
            else:
                second+=1

        return ans
                
        