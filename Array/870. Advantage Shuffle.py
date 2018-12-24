
#https://blog.csdn.net/fuxuemingzhu/article/details/82796298
import collections
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res=[0]*len(A)
        A=collections.deque(sorted(A))
        B=collections.deque(sorted((b,i) for i,b in enumerate(B)))
        for i in range(len(A)):
            a=A.popleft()
            b=B[0]
            if a>b[0]:
                B.popleft()
            else:
                b=B.pop()
            res[b[1]]=a
        return res



