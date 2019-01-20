
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        "首先考虑特殊情况"
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        #定义哑变量
        dummy=ListNode(-1)
        p=dummy
        #遍历l1和l2
        #定义变量jinwei,表示是否进位
        jinwei=0
        while l1 and l2:
            #除以10取余数，当相加为两位数的时候
            p.next=ListNode((l1.val+l2.val+jinwei)%10)
            #判断下一位是否进位
            jinwei=(l1.val+l2.val+jinwei)/10
            #往下遍历
            l1=l1.next
            l2=l2.next
            p=p.next
        #当l1和l2长度不相等的时候
        if l1:
            while l1:
                p.next = ListNode((l1.val + jinwei) % 10)
                jinwei = (l1.val + jinwe) / 10
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + jinwei) % 10)
                jinwei = (l2.val +jinwei) / 10
                l2 = l2.next
                p = p.next

        #当最后一位需要进位的时候，例如 9-9-1，9-9-1
        if jinwei==1:
            p.next=ListNode(1)
        return dummy.next







