"题目：有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。"
"例子 重量[2,2,6,5,4] 价值[6,3,5,4,6]  背包承重 10  输出15"

"递归思路：遍历重量列表，当 当前重量加上历史重量小于背包承重时(cur_cap+w[cur_index]<=cap)，可以把当前物品放进去，得到放入当前物品的价值 use"
"也可以不放进去，就是no use，取use和no use中的大值"
def helper(w,v,n,cur_index,cap,cur_cap,cur_value):
    if cur_index==n:
        return cur_value
    use=0
    if cur_cap+w[cur_index]<=cap:
        use=helper(w,v,n,cur_index+1,cap,cur_cap+w[cur_index],cur_value+v[cur_index])
    no_use=helper(w,v,n,cur_index+1,cap,cur_cap,cur_value)
    return max(use,no_use)

v=[6,3,5,4,6]
w=[2,2,6,5,4]
n=5
cap=10
result=helper(w,v,n,0,cap,0,0)
print(result)

"由暴力递归可知，求解的过程涉及的主要参数(与cur_value互相制约的)是 遍历到第几个位置(cur_index) 和 背包重量(cur_cap）"
"建立 一个二维数组dp,dp[i][j]表示，第i个位置，背包承重为j时的 max value"

def bb(w,v,n,cap):
    dp=[[0 for _ in range(cap+1)] for _ in range(n)]

    for i in range(len(dp[0])):
        if i>=w[0]:
            dp[0][i]=v[0]

    for i in range(1,n):
        for j in range(1,cap+1):
            if j>w[i]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
result1=bb(w,v,n,cap)
print(result1)




