# @Time : 2022-08-04 16:17
# @Author : Phalange
# @File : 剑指 Offer 52. 两个链表的第一个公共节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        myset = set()
        cur = headA
        while cur:
            myset.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in myset:
                break
            cur = cur.next

        return cur


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