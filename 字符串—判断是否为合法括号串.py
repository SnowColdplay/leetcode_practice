"题目"
"对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。"
"给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。"
"测试样例"
"(()())" "返回 true"

def solution(s):
    cnt=0
    for i in range(len(s)):
        if s[i]=="(":
            cnt=cnt+1
        if s[i]==")":
            cnt=cnt-1
    if cnt==0:
        return True
    else:
        return False

s="()a()()"
result=solution(s)
print(result)


