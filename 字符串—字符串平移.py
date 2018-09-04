"题目"
"对于一个字符串，请设计一个算法，将字符串的长度为len的前缀平移到字符串的最后。给定一个字符串A和它的长度，同时给定len，请返回平移后的字符串。"

"测试样例 ABCDE，5，3   返回 DEABC"

"思路：字符串直接索引"
def strpingyi(s,n):
    return s[n:]+s[:n]

s="ABCDE"
n=3
result=strpingyi(s,n)
print(result)