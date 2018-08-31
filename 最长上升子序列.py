"题目"
"给定一个序列A及它的长度n(长度小于等于500)，请返回LIS的长度。"
"LIS(即最长上升子序列)"
"测试样例 [1,4,2,5,3],5，返回3，最长上升子序列是[1,2,3]或者[1,2,5]，len为3"

"动态规划，思路：遍历arr[i]，对于每个arr[i]，从0到i遍历，当满足条件arr[i]比arr[j]大时，说明这是一个上升子序列"

def LIS(alist):
    dp=[0 for _ in range(len(alist))]
    dp[0]=1
    for i in range(len(alist)):
        tmp=0
        for j in range(i):
            if alist[i]>alist[j] and tmp<dp[j]:
                tmp=dp[j]
        dp[i]=tmp+1
    return max(dp)

alist=[1,4,2,5,3]
result=LIS(alist)
print(result)