class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res=0
        i=0
        while i<len(nums):
            res+=nums[i]
            i+=2
        return res
