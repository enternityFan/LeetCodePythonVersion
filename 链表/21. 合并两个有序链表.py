# @Time : 2022-09-08 22:02
# @Author : Phalange
# @File : 21. 合并两个有序链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list2.val > list1.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur1 = list1
            cur2 = list2.next
        cur = head
        while cur1 and cur2 :
            if cur1.val > cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next

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
