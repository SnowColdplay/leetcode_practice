"最大上升子序列和"
"https://blog.csdn.net/hnuzengchao/article/details/8635874"
"例如数组[1,7,3,5,9,4,8]，最大上升子序列和是[1,3,5,9]为18"
"思路是：子问题是，当前位置的最大上升子序列和，是之前的最大上升子序列和，加上当前位置值，从0开始遍历到当前位置,若满足上升条件，则提取maxs"
"状态dp[i]表示以i结尾的递增子序列的和。状态转移方程dp[i] = max(dp[j]) + data[i], 1 <= j < i, 且data[j] < data[i]"

def LIS(alist):
    sums=[]
    sums.append(alist[0])
    for i in range(1,len(alist)):
        maxs=0
        for j in range(i):
            if alist[i]>alist[j]:
                if maxs<sums[j]:
                    maxs=sums[j]
        sums.append(maxs+alist[i])
        print(sums)
    return max(sums)

result=LIS([1,7,3,5,9,4,8])
print(result)