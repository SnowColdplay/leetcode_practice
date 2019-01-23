class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #两个两个一组
        #超时，“23 / 48 test cases passed”
        ab=[]
        for a in A:
            for b in B:
                ab.append(a+b)
        cd=[]
        for c in C:
            for d in D:
                cd.append(c+d)
        cnt=0
        for ab1 in ab:
            for cd1 in cd:
                if ab1+cd1==0:
                    cnt=cnt+1
        return cnt

A=[1,2]
B=[-2,-1]
C=[-1,2]
D=[0,2]

result=Solution().fourSumCount(A,B,C,D)
print(result)

import collections
class Solution1:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #用字典，索引快
        ans=0
        dict=collections.defaultdict(int)
        for a in A:
            for b in B:
                dict[a+b]+=1
        for c in C:
            for d in D:
                ans += dict[-(c + d)]
        return ans



result=Solution1().fourSumCount(A,B,C,D)
print(result)


