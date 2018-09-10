"题目"
"判断两个字符串是否同构字符串"
"例如 aba,xyx 是同构字符串"
"aba,xyz 不是同构字符串"


"可以提取到 后面重复出现的字符，最开始的index"
def isomorphic(t):
    s = []
    d = {}
    for i in range(len(t)):
        if t[i] not in d:
            d[t[i]] = i
        s.append(d[t[i]])
    return s

t="aba"
result1=isomorphic(t)
print(result1)
t1="xyx"
result2=isomorphic(t1)
print(result2)


"方法2，利用zip函数"
def isomorphic1(s,t):
    print(set(zip(s, t)))
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

s="abc"
t="xyz"
result3=isomorphic1(s,t)
print(result3)

