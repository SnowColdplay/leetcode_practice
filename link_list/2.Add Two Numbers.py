# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_link(alist):
    "定义一个头节点，和temp节点，temp节点遍历"
    temp_node=ListNode(alist[0])
    node=ListNode(-1)
    node.next=temp_node
    for val in alist[1:]:
        temp_node.next=ListNode(val)
        temp_node=temp_node.next
    print(node.next)
    return node.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #遍历l1和l2，将val储存在list里,然后用reverse倒叙
        list_l1=[]
        while l1:
            list_l1.append(l1.val)
            l1=l1.next
        list_l2=[]
        while l2:
            list_l2.append(l2.val)
            l2=l2.next
        #列表反转
        list_l1.reverse()
        list_l2.reverse()
        print(list_l1)
        print(list_l2)
        #将长度小的，左边补全0
        if len(list_l1)>len(list_l2):
            for i in range(len(list_l1)-len(list_l2)):
                list_l2.insert(0,0)
        elif len(list_l2)>len(list_l1):
            for i in range(len(list_l2)-len(list_l1)):
                list_l1.insert(0,0)
        #相加
        list_sum=[]
        #倒叙索引，从len(list_l1)到-1，间隔-1
        for i in range(len(list_l1)-1,-1,-1):
            print(i)
            add=list_l1[i]+list_l2[i]
            if i==len(list_l1)-1:
                add_next=0
            #当前位的求和，加上上前一位为0时的情况(+1)
            add=add+add_next
            if add%10==0:
                add=0
                add_next=1
            list_sum.append(add)
        print(list_sum)

        #将值写入链表中
        l3=list_to_link(list_sum)
        return l3

#构造两个链表
node1=ListNode(2)
node2=ListNode(4)
node3=ListNode(3)

node11=ListNode(5)
node22=ListNode(6)
node33=ListNode(4)

node1.next=node2
node2.next=node3
node3.next=None

node11.next=node22
node22.next=node33
node33.next=None

#将两个链表放入solution中
result=Solution().addTwoNumbers(node1,node11)
print(result.val)
print(result.next.next.val)

"审题错误，不一定两个链表长度相同"
"没考虑 input [5] [5],output[0,1]的情况"
"不用转化为list,直接在链表上相加即可"


