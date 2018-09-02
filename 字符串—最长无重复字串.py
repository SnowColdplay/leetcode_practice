"题目"
"对于一个字符串,请设计一个高效算法，找到字符串的最长无重复字符的子串长度"

"测试样例 aabcb ，返回 3"

"遍历字符串，求s[i]最长无重复字串，先计算s[i-1]，如果s[i]在之前出现过，则是 i-start+1"

def solution(s):
    start=0
    maxlen=0
    position={}
    for i in range(len(s)):
        if s[i] in position and position[s[i]]>=start:
            start=position[s[i]]+1
        position[s[i]]=i

        curlen=i-start+1
        maxlen=max(maxlen,curlen)
    return maxlen

