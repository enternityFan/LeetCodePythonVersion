# @Time : 2022-08-04 17:06
# @Author : Phalange
# @File : 剑指 Offer 22. 链表中倒数第k个节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head

        while cur:
            n +=1
            cur = cur.next
        cur = head
        idx = 0
        while n - idx != k:
            idx +=1
            cur = cur.next

        return cur


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        idx = 0
        # 快指针先走k步
        while idx <k:
            fast = fast.next
            idx +=1

        while fast:
            fast = fast.next
            slow = slow.next
        return slow