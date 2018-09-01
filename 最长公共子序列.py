"最长相关"
"https://www.cnblogs.com/aademeng/articles/7405526.html"
'https://www.cnblogs.com/aademeng/articles/7405536.html'
def LCSdigui(A,B,i,j):
    if i>len(A)-1 or j>len(B)-1:
        return 0      #注意边界条件是 i>len(A)-1 而不是i>=len(A)-1，因为当i=len(A)-1的时候还是可以比较的
    if A[i]==B[j]:
        return 1+LCSdigui(A,B,i+1,j+1)
    if A[i]!=B[j]:
        if LCSdigui(A,B,i+1,j)>LCSdigui(A,B,i,j+1):
            return LCSdigui(A,B,i+1,j)
        else:
            return LCSdigui(A,B,i,j+1)


a="1A2C3D4B56"
b="B1D23CA45B6A"


"由上面的暴力递归可知，整个过程是对字符串A和B的遍历"
"建立dp,dp[i][j]表示，字符串A[:i]和B[:j]，的最长公共子序列"
def LCSdp(A,B):
    n=len(A)
    m=len(B)
    dp=[[0 for _ in range(m)] for _ in range(n)]

    "初始条件是，dp[0][j] A[0]与B比较"
    "dp[i][0]是 A与B[0]比较"

    for j in range(m):
        if A[0]==B[j]:
            for jj in range(j,m):
                dp[0][jj]=1
    for i in range(n):
        if B[0]==A[i]:
            for ii in range(i,n):
                dp[ii][0]=1

    for i in range(1,n):
        for j in range(1,m):
            if A[i]==B[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]


result=LCSdigui(a,b,0,0)
print(result)

result1=LCSdp(a,b)
print(result1)