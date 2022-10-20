#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：82. 删除排序链表中的重复元素 II.py
@Author ：HuntingGame
@Date ：2022-10-20 8:42 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        repeat = set()
        # 第一步，去重,并找到重复的元素
        while cur and cur.next:
            if cur.val == cur.next.val:
                repeat.add(cur.val)
                cur.next = cur.next.next
            cur = cur.next
        # 第二步，去掉重复过的元素
        cur = head
        prev = None
        # 首先找到头结点
        while cur and cur.val in repeat:
            prev = cur
            cur = cur.next
        #现在找到了头结点
        if prev:
            prev.next = None
        head = cur
        cur = head
        prev = None
        while cur:
            print(cur.val)
            if cur.val in repeat:
                prev.next = cur.next
            else:

                prev = cur
            cur = cur.next



        return head

head = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
head2 = ListNode(1,ListNode(2,ListNode(2)))
print(Solution().deleteDuplicates(head2))