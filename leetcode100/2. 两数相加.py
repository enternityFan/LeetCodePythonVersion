#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2. 两数相加.py
@Author ：HuntingGame
@Date ：2023-02-01 9:38 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next









class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        思路一，利用链表每一位的去加,到最后再反转一下链表；也可以不逆序，需要记录一下头结点不过；
        :param l1:
        :param l2:
        :return:
        """
        ca = 0
        n1 = 0
        n2 = 0
        n = 0
        c1 = l1
        c2 = l2
        node = None
        pre = None

        while c1 is not None or c2 is not None:
            n1 = c1.val if c1 is not None else 0
            n2 = c2.val if c2 is not None else 0
            n = n1 + n2 + ca
            pre = node
            node = ListNode(n%10)
            node.next = pre
            ca = n // 10
            c1 = c1.next if c1 is not None else None
            c2 = c2.next if c2 is not None else None

        #查看会不会多出一个进位的节点
        if ca == 1:
            pre = node
            node = ListNode(1)
            node.next = pre
        return self.reverseList(node)

    def reverseList(self, head):
        """
        反转链表
        :param node:
        :return:
        """
        cur = head
        if cur is None:
            return None
        pre = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #TODO
        思路二，首先把链表变化为列表，然后做加法，再然后去变为链表
        :param l1:
        :param l2:
        :return:
        """