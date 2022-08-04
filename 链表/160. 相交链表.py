# @Time : 2022-08-04 16:21
# @Author : Phalange
# @File : 160. 相交链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

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