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
RMB=[1,2,3]
result=helper(target,index,start,RMB)
print(result)
