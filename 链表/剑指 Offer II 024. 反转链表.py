# @Time : 2022-08-04 17:13
# @Author : Phalange
# @File : 剑指 Offer II 024. 反转链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return cur
