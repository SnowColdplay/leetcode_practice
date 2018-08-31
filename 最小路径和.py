"题目：有一个矩阵map，它每个格子有一个权值。从左上角的格子开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。"
"给定一个矩阵map及它的行数n和列数m，请返回最小路径和。保证行列数均小于等于100."

"暴力递归"
def digui(matrix,i,j):
    if i==len(matrix)-1 and j==len(matrix[0])-1:
        return matrix[-1][-1]
    if i==len(matrix)-1 and j<len(matrix[0])-1:
        return matrix[i][j]+digui(matrix,i,j+1)
    if i<len(matrix)-1 and j==len(matrix[0])-1:
        return matrix[i][j]+digui(matrix,i+1,j)
    return matrix[i][j]+min(digui(matrix,i+1,j),digui(matrix,i,j+1))
matrix=[[1,2,3],[1,1,1]]
result=digui(matrix,0,0)
print(result)

"动态规划"
def matrixdp(matrix):
    dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dp[0][0]=matrix[0][0]
    for i in range(1,len(matrix)):
        dp[i][0]=dp[i-1][0]+matrix[i][0]
    for i in range(1,len(matrix[0])):
        dp[0][i]=dp[0][i-1]+matrix[0][i-1]

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+matrix[i][j]
    return dp[-1][-1]


result1=matrixdp(matrix)
print(result1)










# "----------------------------错误的dfs递归枚举----------------------------"
# "想枚举出每条路径，试一试dfs，但是结果很诡异？？？求大佬点播"
# def helper(matrix,n,m,cur_n,cur_m,result,each_result):
#     if cur_m==m-1 and cur_n==n-1:
#         result.append(each_result)
#     if cur_n+1<n and cur_m<m:
#         each_result.append(matrix[cur_n + 1][cur_m])
#         helper(matrix,n,m,cur_n+1,cur_m,result,each_result)
#     if cur_n<n and cur_m+1<m:
#         each_result.append(matrix[cur_n][cur_m + 1])
#         helper(matrix, n, m, cur_n ,cur_m+1, result, each_result)
#
# def lujing(matrix,n,m):
#     result=[]
#     helper(matrix,n,m,0,0,result,[matrix[0][0]])
#     return result
#
# matrix=[[1,2,3],[4,5,6]]
# n=2
# m=3
# result=[]
# each_result=[]
# result1=lujing(matrix,n,m)
# print(result1)
# "--------------------------------------------------------------------------"
