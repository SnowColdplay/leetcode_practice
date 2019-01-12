from collections import Counter
"用counter的dict,如果没有这个数的话，就是0"

"https://blog.csdn.net/qq_17550379/article/details/85051342"

"更新dict[2*i] -= dict[i]。为什么呢？因为可能出现这种情况{1:1, 2:2, 4:1}"
class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A_dict = Counter(A)
        print(A_dict)
        for x in sorted(A_dict, key=lambda x: abs(x)):
            print(x)
            print(A_dict[10])
            if A_dict[x] > A_dict[2 * x]:
                return False
            A_dict[2 * x] -= A_dict[x]
        return True

result=Solution().canReorderDoubled([3,1,3,6])
print(result)