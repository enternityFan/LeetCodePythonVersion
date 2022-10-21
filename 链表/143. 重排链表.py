#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：143. 重排链表.py
@Author ：HuntingGame
@Date ：2022-10-18 20:55 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        #1.找中点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #2.反转后半部分的链表
        cur = slow.next
        head2 = slow.next
        slow.next = None
        prev = None
        while cur:
            if prev:
                print(prev.val)
            print(cur.val)

            tmp  = cur.next.next if cur.next else None
            cur.next.next = cur
            cur.next = prev
            prev = cur.next
            cur = tmp
        # 3.连接
        cur1 = head
        cur2 = head2
        while cur1 and cur2:
            tmp1 = cur1.next
            tmp2 = cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1 = tmp1
            cur2 = tmp2
        return head




