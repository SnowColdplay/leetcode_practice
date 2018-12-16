# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:33:37 2018

@author: snow
"""


#暴力法,从前往后遍历，遇到重复的，就从重复的后面一个开始
#986 / 987 test cases passed.有一个超时
class Solution:
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
                    if ss[j]==s[i+1]:
                        ss=ss[j+1:]
                        break
        return res
result=Solution().lengthOfLongestSubstring("pwwkew")
print(result)
            