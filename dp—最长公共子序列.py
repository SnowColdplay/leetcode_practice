
"最长相关"
"https://www.cnblogs.com/aademeng/articles/7405526.html"
'https://www.cnblogs.com/aademeng/articles/7405536.html'
def LCS(A,B,n,m):
    if n<=0 or m<=0:
        return 0
    if A[n]==B[m]:
        return LCS(A,B,n-1,m-1)+1
    if A[n]!=B[m]:
        if LCS(A,B,n-1,m)>LCS(A,B,n,m-1):
            return LCS(A,B,n-1,m)
        else:
            return LCS(A,B,n,m-1)


a='1A2C3D4B56'
n=len(a)-1

b='B1D23CA45B6A'
m=len(b)-1

result=LCS(a,b,n,m)
print(result)


