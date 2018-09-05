"题目"
"有一个升序数组，在某位置重新排列了，例如 [0,1,2,3,4,5,6,7] 重排为 [4,5,6,7,0,1,2]"
"找到它最小的元素"

"思路 二分"
"如果nums[0]<nums[-1],说明没有改变顺序，直接返回nums[0]"
"看中间值，中间值或者比left大，或者比left小"
"中间值比left大，说明从left到mid这段是递增的，从mid到right找，令left=mid"
"中间值比left小，说明left到mid这段是先增后减小的,从left到mid找,令mid=right"
"循环条件为left<right，最后返回nums[left]，nums[right]中较小的"

"递增的序列一般是left=mid+1，right=mid-1,但是此题不是递增序列"

def findMin(nums):
    left=0
    right=len(nums)-1
    if nums[left] < nums[right]:
        return nums[left]

    while left<right:
        mid=left+(right-left)//2
        if nums[mid]>nums[left]:
            left=mid
        elif nums[mid]<nums[left]:
            right=mid
        elif nums[mid]==nums[left]:
            break
    return min(nums[left],nums[right])

nums=[3,4,5,1,2]
result=findMin(nums)
print(result)

