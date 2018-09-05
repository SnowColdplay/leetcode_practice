"题目"
"给出一个有序数组，和一个target,返回target的index（如果target在数组里),返回应该插入的位置(如果target不在数组里)"
"测试用例 [1,3,5,6], 5，返回2"
"测试用例 [1,3,5,6], 2，返回1"

"思路：二分"
"循环条件是要left<=right而不是left<right。因为若当target大于最大值的时候，[1,3,5,6] 7.最后是left=3,right=3,mid=3,返回mid+1，就出去了。"
"如果只是left<right，最后出不去"

def searchInsert(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return left

nums=[1,3,5,6]
target=7
result=searchInsert(nums,target)
print(result)