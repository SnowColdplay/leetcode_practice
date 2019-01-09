"暴力法：853 / 856 test cases passed."
"对nums进行遍历"
"暴力法：853 / 856 test cases passed."

class Solution1:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0   #保留结果
        for i in range(len(nums)):
            s=[]
            for j in range(i,len(nums)):
                if j==i:   #开始
                    s.append(nums[j])
                else:
                    n=s[-1]
                    if nums[n] not in s:
                        s.append(nums[n])
                    else:
                        continue
            if len(s)>cnt:
                cnt=len(s)
        return cnt

result=Solution1().arrayNesting([5,4,0,3,1,6,2])
print(result)

"保留已经得到过的s，如果数字已经在s中出现过，就不用再遍历了"
"时间和空间复杂度o(n)"
"854 / 856 test cases passed."

class Solution2:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        ss=[]
        for i in range(len(nums)):

            if nums[i] in ss:
                continue

            s=[]
            for j in range(i,len(nums)):
                if j==i:
                    s.append(nums[j])
                else:
                    n=s[-1]
                    if nums[n] not in s:
                        s.append(nums[n])
                    else:
                        continue
            ss.extend(s)
            print(s)
            if len(s)>cnt:
                cnt=len(s)
        return cnt

result=Solution2().arrayNesting([2,0,1])
print(result)

"用while循环，通过"

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [0]*len(nums)
        res = 0
        for i in range(len(nums)):
            if seen[i] != -1:
                j = i
                count = 0
                while seen[j] != -1:
                    count += 1
                    seen[j] = -1
                    j = nums[j]
                res = max(res, count)
        return res

result=Solution().arrayNesting([2,0,1])
print(result)