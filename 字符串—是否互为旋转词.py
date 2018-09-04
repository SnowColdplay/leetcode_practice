"题目"
"如果对于一个字符串A，将A的前面任意一部分挪到后边去形成的字符串称为A的旋转词。" \
"比如A=12345,A的旋转词有12345,23451,34512,45123和51234。对于两个字符串A和B，请判断A和B是否互为旋转词。"

"思路：KMP算法 字符串匹配算法，核心思想是   利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的"

"过程"
"1.计算匹配串的前缀表。"
"例如是 ababc ,他的子串是 a ab aba abab ababc,前缀表是前面和后面的字符相等的长度，对于这几个子串来说，前缀表的计算如下"
"a: 0"
"ab: 前缀a,后缀b,相等长度为0"
"aba，前缀a,后缀a，相等长度为1"
"abab,前缀ab,后缀ab,相等长度为2"
"ababc，相等长度为0"
"不算最后一个，前面添加一个 -1（表示空字串)，前缀表为[-1,0,0,1,2]"

def checkRotation(A,B):
    if len(A)!=len(B):
        return False
    C=A+A
    return kmp(C,B)

def kmp(big,small):
    i=0
    while i<len(big)-len(small)+1:
        "从前往后匹配"
        match=True
        for j in range(len(small)):
            if big[i+j]!=small[j]:  #如果当前匹配下big[j]!=small[j]，说明当前匹配无法匹配，令match为false.并且break，移动字符串
                match=False
                break
        if match:                  #如果match为True 说明匹配成功，返回
            return True
        if j:
            i=i+j-pretable(small[:j])   #如果有部分匹配，移动位置=已匹配字符串-对应部分匹配值
        else:
            i=i+1                       #如果没有匹配部分，移动1位就ok
    return False


"计算当前元素之前的 前缀表数值"
def pretable(s):
    pre=[s[:i+1] for i in range(len(s)-1)]
    post=[s[i+1:] for i in range(len(s)-1)]
    inter=list(set(pre)&set(post))
    if inter:
        return len(inter[0])
    else:
        return 0

A="cdab"
B="abcd"
result=checkRotation(A,B)
print(result)
