"题目"
"给一个升序数组，和一个target，返回target的开始和终止位置，如果没有，则返回[-1,-1]"
"测试用例 nums = [5,7,7,8,8,10], target = 8"
"返回 [3,4]"
"测试用例  nums = [5,7,7,8,8,10]，target=6"
"返回 [-1,-1]"

"要求时间复杂度为O(log n)"

"思路，复杂度为O(log n)，则想到用二分"
"注意：循环条件要left<=right，而不是left<right，left<right有一些case无法通过，如"
"[1] 1,这种情况，输出为[0,0]，是left==right条件下的"

def searchRange(nums, target):
    left=0
    right=len(nums)-1

    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        elif nums[mid]==target:
            ans=[0,0]
            if nums[left]==target:
                ans[0]=left
            if nums[right]==target:
                ans[1]=right
            for i in range(mid,right+1):
                if nums[i]==target:
                    ans[1]=i
            for i in range(mid,left-1,-1):
                if nums[i]==target:
                    ans[0]=i
            return ans
    return [-1,-1]


nums=[5,7,7,8,8,10]
target=8
result=searchRange(nums,target)
print(result)