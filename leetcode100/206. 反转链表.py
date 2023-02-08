#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：206. 反转链表.py
@Author ：HuntingGame
@Date ：2023-02-08 9:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        next = None
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
