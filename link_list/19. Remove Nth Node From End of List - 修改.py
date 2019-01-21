# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#定义两个指针
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #定义两个指针，cur和pre，都指向dummy
        dummy=ListNode(0)
        dummy.next=head
        pre=cur=dummy
        #cur先向前走n步
        while n:
            cur=cur.next
            n=n-1
        #cur和pre同时向前走
        while cur and cur.next:
            cur=cur.next
            pre=pre.next
        #跳过目标值
        pre.next = pre.next.next
        return dummy.next


#构造链表
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

result=Solution().removeNthFromEnd(node1,2)
print(result.val)

"无法考虑只有一个节点的时候"


