# @Time : 2022-08-04 21:31
# @Author : Phalange
# @File : 剑指 Offer 06. 从尾到头打印链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        cur = prev
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        cur = prev
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur =tmp


        return arr