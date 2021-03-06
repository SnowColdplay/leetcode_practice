
"暴力法,复杂度o(n^3)"
"249 / 313 test cases passed 果断是超时的"
class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    ans=nums[i]+nums[j]+nums[k]
                    if ans==0:
                        res.append([nums[i],nums[j],nums[k]])
        result=[]
        for i in range(len(res)):
            if res[i] not in result:
                result.append(res[i])
        return result
# result=Solution1().threeSum([-1, 0, 1, 2, -1, -4])
# print(result)

"双指针法，时间复杂度 o(n^2)"
"311 / 313 test cases passed.超时"
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]==0 and [nums[i],nums[left],nums[right]] not in res:
                    res.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                elif nums[left]+nums[right]+nums[i]>0:
                    right=right-1
                elif nums[left]+nums[right]+nums[i]<0:
                    left=left+1
                else:
                    left=left+1
                    right=right-1
        return res
# result=Solution2().threeSum([-1, 0, 1, 2, -1, -4])
# print(result)

"对于上面的代码，有一个地方可以优化，有重复元素的时候，直接跳过，而不是重新再搜索一遍"
class Solution3:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)-2):
            #跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[right]==nums[right-1]:
                        right=right-1
                    while left<right and nums[left]==nums[left+1]:
                        left=left+1
                    left=left+1
                    right=right-1
                elif nums[left]+nums[right]+nums[i]>0:
                    right=right-1
                elif nums[left]+nums[right]+nums[i]<0:
                    left=left+1
        return res

result=Solution3().threeSum([-2,0,0,2,2])
print(result)


