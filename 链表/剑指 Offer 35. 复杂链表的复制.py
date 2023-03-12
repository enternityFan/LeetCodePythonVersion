#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 35. 复杂链表的复制.py
@Author ：HuntingGame
@Date ：2023-03-12 10:16 
C'est la vie!!! enjoy ur day :D
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        next = None
        # 下面的while做的操作:
        # 1->2->3
        # 1->1'->2'->3'
        while cur:
            next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = next
            cur = next
        cur = head
        copy = None
        # 1 1' 2 2' 3 3'
        # 下面是在依次设置1' 2' 3'的random指针
        while cur:
            next = cur.next.next
            copy = cur.next
            copy.random = cur.random.next if cur.random else None

            cur = next
        # 下面代码分离1和1'
        cur = head
        res = cur.next

        while cur:
            next = cur.next.next
            copy = cur.next
            cur.next = next
            copy.next = next.next if next else None
            cur = next
        return res