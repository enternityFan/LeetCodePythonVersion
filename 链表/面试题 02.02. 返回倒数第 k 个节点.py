# @Time : 2022-08-04 17:11
# @Author : Phalange
# @File : 面试题 02.02. 返回倒数第 k 个节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        idx = 0
        fast = head
        slow = head
        while idx <k:
            fast = fast.next
            idx +=1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val