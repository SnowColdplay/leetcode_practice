"题目"
"对于一个给定的字符串数组，请找到一种拼接顺序，使所有小字符串拼接成的大字符串是所有可能的拼接中字典序最小的"
"给定一个字符串数组strs，同时给定它的大小，请返回拼接成的串。"



def findsmall(strs):
    for i in range(1,len(strs)):
        for j in range(i):
            if strs[i]+strs[j]<strs[j]+strs[i]:
                strs[i],strs[j]=strs[j],strs[i]
    return "".join(strs)

strs=["abc","de"]
result=findsmall(strs)
print(result)