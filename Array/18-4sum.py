
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        res=[]
        dict={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] not in dict:
                    dict[nums[i]+nums[j]]=[(i,j)]
                else:
                    dict[nums[i] + nums[j]].append((i,j))
        print(dict)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                T=target-nums[i]-nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0]>j: #这个条件，保证排除自身
                         res.append((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return list(set(res))

result=Solution().fourSum([1, 0, -1, 0, -2, 2],0)
print(result)





