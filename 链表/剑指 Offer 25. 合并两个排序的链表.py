# @Time : 2022-09-08 21:45
# @Author : Phalange
# @File : 剑指 Offer 25. 合并两个排序的链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            head = l1
            cur1 = l1.next
            cur2 = l2
        else:
            head = l2
            cur1 = l1
            cur2 = l2.next
        cur = head
        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next

            print(cur.val)
            if cur.next:
                cur = cur.next

        while cur1:
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next

        while cur2:
            cur.next = cur2
            cur2 = cur2.next
            cur = cur.next

        return head
