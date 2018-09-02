"题目"
"请编写一个方法，将字符串中的空格全部替换为“%20”。假定该字符串有足够的空间存放新增的字符，并且知道字符串的真实长度(小于等于1000)，同时保证字符串由大小写的英文字母组成。"
"测试用例"
"Mr John Smith ，返回 Mr%20John%20Smith"

"利用python replace函数"
def tihuan(s):
    s=s.replace(" ","%20")
    return s

s="Mr John Smith"
result=tihuan(s)
print(result)


"遍历法"
def tihuan1(s):
    ss=""
    for i in range(len(s)):
        if s[i]==" ":
            ss=ss+"%20"
        else:
            ss=ss+s[i]
    return ss

result2=tihuan1(s)
print(result2)





