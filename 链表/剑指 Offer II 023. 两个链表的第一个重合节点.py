# @Time : 2022-08-04 16:06
# @Author : Phalange
# @File : 剑指 Offer II 023. 两个链表的第一个重合节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m = 0
        n = 0
        cur1 = headA
        while cur1:
            cur1 = cur1.next
            m +=1
        cur2 = headB
        while cur2:
            cur2 = cur2.next
            n +=1
        cur1 = headA if m > n else headB
        cur2 = headA if m <=n else headB
        err = abs(m - n)
        idx = 0
        while cur1 and idx < err:
            idx +=1
            cur1 = cur1.next

        while cur2 and cur1:
            if cur1 == cur2:
                break
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1



rootA = ListNode(4)
rootA.next = ListNode(1)
rootA.next.next = ListNode(8)
rootA.next.next.next = ListNode(4)
rootA.next.next.next.next = ListNode(5)

rootB = ListNode(5)
rootB.next = ListNode(0)
rootB.next.next = ListNode(1)
rootB.next.next.next = rootA.next.next
print(Solution().getIntersectionNode(rootA,rootB))