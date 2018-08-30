"题目:有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数aim(小于等于1000)代表要找的钱数，求换钱有多少种方法。"
"例子：  [1,2,4],3,3   返回2"

"http://www.bubuko.com/infodetail-782490.html"
"递归解法"
def helper(target,index,start,RMB):
    if RMB[index]==start:
        return 1
    return helper(target-RMB[index],index-1,start,RMB)+helper(target,index-1,start,RMB)

target=3
index=1
start=1
RMB=[1,2,4]
result=helper(target,index,start,RMB)
print(result)

"通过递归可知，影响最终结果的因素主要是：对array的遍历，array[i]，以及target的值"
"因此可建立dp矩阵,dp[i][j]，代表array[i]位置为止，目标值为j的count,dp[-1][-1]即为所求"

def cntways(array,target):
    n=len(array)

    dp=[[0 for _ in range(target+1)] for _ in range(n)]

    for j in range(len(dp[0])):
        if j%array[0]==0:
            dp[0][j]=1
    for i in range(len(dp)):
        dp[i][0]=1

    for i in range(1,n):
        for j in range(1,target+1):
            if j<array[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-array[i]]
    return dp[-1][-1]
"优化方案：可先对array进行筛选，只遍历到array[i]小于target的位置"
result1=cntways(RMB,3)
print(result1)





