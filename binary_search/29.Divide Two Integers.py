
class Solution1(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #除法的本质：被除数-除数
        #分情况讨论，除数和被除数大于小于0的时候
        #超时
        cnt = 0
        if dividend>0 and divisor>0:
            while dividend>=divisor:
                dividend=dividend-divisor
                cnt=cnt+1
            return cnt
        elif dividend>0 and divisor<0:
            divisor=-divisor
            while dividend>=divisor:
                dividend=dividend-divisor
                cnt=cnt+1
            return -cnt
        elif dividend<0 and divisor>0:
            dividend=-dividend
            while dividend>=divisor:
                dividend=dividend-divisor
                cnt=cnt+1
            return -cnt
        elif dividend<0 and divisor<0:
            dividend=-dividend
            divisor=-divisor
            while dividend >=divisor:
                dividend = dividend - divisor
                cnt = cnt + 1
            return cnt
        elif dividend==0:
            return 0
"https://www.cnblogs.com/zuoyuan/p/3779359.html"
class Solution1(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        count = 0
        res = 0
        #首先转化为绝对值形式
        a=abs(dividend)
        b=abs(divisor)
        while a>=b:
            sum=b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        #加这个才能ac
        if res > 2147483647:
            return 2147483647
        return res




result=Solution1().divide(1,-1)
print(result)







