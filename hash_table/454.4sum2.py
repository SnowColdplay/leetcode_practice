"20 / 48 test cases passed."
"暴力，果然超时"
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        if A[i]+B[j]+C[k]+D[l]==0:
                            res=res+1
        return res
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [0, 2]
res=Solution().fourSumCount(A,B,C,D)
print(res)

"用字典，将两个数储存在一起"
"https://blog.csdn.net/fuxuemingzhu/article/details/79473739"
from collections import Counter
AB = Counter(a + b for a in A for b in B)
print((AB[-c-d] for c in C for d in D))