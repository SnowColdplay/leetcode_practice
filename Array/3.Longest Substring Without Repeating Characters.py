# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:33:37 2018

@author: snow
"""


"暴力法,从前往后遍历，遇到重复的，就从重复的后面一个开始"
"986 / 987 test cases passed.有一个超时"
class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        res=0
        ss=""
        for i in range(len(s)):
            ss=ss+s[i]
            print('ss',ss)
            res1=len(ss)
            if res1>res:
                res=res1
            if i<len(s)-1 and s[i+1] in ss:
                for j in range(len(ss)):
                    if ss[j]==s[i+1]:  #遇到重复的从重复后一个位置开始
                        ss=ss[j+1:]
                        break
        return res
#==============================================================================
# result=Solution1().lengthOfLongestSubstring("pwwkew")
# print(result)
#=============================================================================
"可用字典结构，对寻找重复出现的位置索引，这样省去了对位置的遍历"
class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        res=0
        dict={}
        for i in range(len(s)):
            if s[i] in dict and start<dict[s[i]]+1:
                start=dict[s[i]]+1
            else:
                res=max(res,i-start+1)
            dict[s[i]]=i
            print(dict)
            print(start)
        return res
            
result=Solution2().lengthOfLongestSubstring("abcabcbb")
print(result)
            