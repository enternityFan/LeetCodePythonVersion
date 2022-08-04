# @Time : 2022-08-04 21:32
# @Author : Phalange
# @File : 剑指 Offer 24. 反转链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev