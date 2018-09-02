"题目"
"对于两个字符串A和B，我们需要进行插入、删除和修改操作将A串变为B串，定义c0，c1，c2分别为三种操作的代价，请设计一个高效算法，求出将A串变为B串所需要的最少代价。" \
"给定两个字符串A和B，及它们的长度和三种操作代价，请返回将A串变为B串所需要的最小代价。保证两串长度均小于等于300，且三种代价值均小于等于100。"

"递归"
"思路分析：分两种大情况，A[i]=B[j]时，比较A[i+1]与B[j+1]"
"当A[i]!=B[j]时，再分三种情况讨论"
"1.将A[i]删除，比较A[i+1]与B[j],代价为c1"
"2.将B[j]删除，比较A[i]与B[j+1]。这步操作相当于在A[i]中插入元素,代价为c0"
"3.直接替换，令A[i]=B[j]，比较A[i+1]与B[j+1],代价为c2"

def digui(A,B,i,j,c0,c1,c2):
    "终止条件是，当A或者B遍历到终点时，代价为 插入操作 ，index的差，乘以单位代价值"
    if i==len(A)-1 or j==len(B)-1:
        return abs((j-i))*c0

    if A[i]==B[j]:
        return digui(A,B,i+1,j+1,c0,c1,c2)

    if A[i]!=B[j]:
        x1=digui(A,B,i+1,j,c0,c1,c2)+c1
        x2=digui(A,B,i,j+1,c0,c1,c2)+c0
        x3=digui(A,B,i+1,j+1,c0,c1,c2)+c2
        return min(min(x1,x2),x3)

A="bbca"
B="cabacab"

result1=digui(A,B,0,0,1,2,7)
print(result1)

"动态规划"
"思路分析：dp[i][j]代表到A[i]和B[j]为止，最小代价函数"
"将A和B前面加上一个空格，方面赋予初始值"
"状态转移方程如上面递归分析所示"

def mincost(A,B,c0,c1,c2):

    dp=[[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

    for i in range(len(dp)):
        dp[i][0]=i*c1
    for j in range(len(dp[0])):
        dp[0][j]=j*c0

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if A[i-1]==B[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                x1=dp[i-1][j]+c1
                x2=dp[i][j-1]+c0
                x3=dp[i-1][j-1]+c2
                dp[i][j]=min(min(x1,x2),x3)

    return dp[-1][-1]

result2=mincost(A,B,1,2,7)
print(result2)



