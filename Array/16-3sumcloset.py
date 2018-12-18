class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=sum(nums[:3])
        diff=abs(target-sum(nums[:3]))
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                val=nums[i]+nums[left]+nums[right]
                diff1=abs(target-val)
                if diff1<diff:
                    res=val
                    diff=diff1
                if res==target:
                    return res   #如何移动指针
                elif val<target:
                    left=left+1
                else:
                    right=right-1
        return res

result=Solution().threeSumClosest([0,2,1,-3],1)
print(result)


