#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：141. 环形链表.py
@Author ：HuntingGame
@Date ：2023-02-06 11:29 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow !=fast:
            if fast.next is None or fast.next.next == None:
                return None
            fast = fast.next.next
            slow = slow.next

        fast = head
        while slow !=fast:
            slow = slow.next
            fast = fast.next

        return slow