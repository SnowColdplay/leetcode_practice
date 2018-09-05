"题目"
"有一个升序数组，在某位置重新排列了，例如 [0,1,2,3,4,5,6,7] 重排为 [4,5,6,7,0,1,2]"
"找到它最小的元素"
"注意，这个题目与上一题不同的是，这个题目是有重复数组"
"{2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2} 和 {2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2},无法判断舍掉哪边"
"这种情况下，当nums[mid]等于nums[left]时，令left=left+1，移动1位，避开相等的情况"
"当遇到nums[left] < nums[right]的情况时，直接返回nums[left]"


def findMin(nums):
    left=0
    right=len(nums)-1

    if nums[left] < nums[right]:
        return nums[left]

    while left<right:
        mid=left+(right-left)//2
        #当nums[mid]等于nums[left]时，令left=left+1，移动1位，避开相等的情况
        if nums[mid]==nums[left]:
            left=left+1
        #当遇到nums[left] < nums[right]的情况时，直接返回nums[left]
        elif nums[left]<nums[right]:
            return nums[left]
        elif nums[mid]>nums[left]:
            left=mid
        elif nums[mid]<nums[left]:
            right=mid
        elif nums[mid]==nums[left]:
            break

    return min(nums[left], nums[right])
nums=[2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2]
result=findMin(nums)
print(result)
