
"collections import Counter 结构"
"https://blog.csdn.net/fuxuemingzhu/article/details/80526298"

from collections import Counter
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counters=collections.Counter()
        count=0
        for row in wall:
            left=0
            for i in range(len(row)-1):
                left+=row[i]
                counters.update([left])
                count=max(count,counters[left])
        return len(wall)-count











