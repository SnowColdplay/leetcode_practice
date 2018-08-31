"题目：有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。"

"递归，思路：登上n阶台阶问题可以转换成登上n-2个台阶方式和登上n-1个台阶方式之和的问题”"
" f(n)=f(n-1)+f(n-2)  (n>2)， f(1)=1;f(2)=2;"

def jump1(n):
    if n==1 or n==2:
        return n
    return jump1(n-1)+jump1(n-2)

"动态规划版本"
"总结：递归的终止条件，通常是动态规划的初始值," \
"递归是从后往前考虑(或从后往前考虑)，把大问题转化为小问题，当小问题不能再小时，就是终止条件"
"将暴力递归转化为dp时，注意递归终止条件和dp初始条件之间的关系"

def jump1dp(n):
    dp=[0 for _ in range(n)]
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

"跳台阶进阶版本：跳台阶有n中方式，1.一次跳一个，2.一次跳两个， * 。。。。* n.一次跳n个"
"递归思路：登上n阶台阶问题可以转换成登上n-2个台阶方式加上登上n-1个台阶加上登上n-3个台阶....加到登上1个台阶方式之和再加上一次登上总台阶和的问题"
"f(n)=f(n-1)+f(n-2) +f(n-3)+......+f(3)+f(2)+(1)+1 "

def jump2(n):
    if n==1 or n==2:
        return n
    cnt=0
    for i in range(1,n):
        cnt=jump2(n-i)+cnt
    return cnt+1

"动态规划版本"
def jump2dp(n):
    dp = [0 for _ in range(n)]
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        for j in range(i):
            dp[i]=dp[j]+dp[i]
        dp[i]=dp[i]+1
    return dp[-1]

result=jump2(10)
result1=jump2dp(10)
print(result)
print(result1)




