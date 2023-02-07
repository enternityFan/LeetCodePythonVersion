#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：160. 相交链表.py
@Author ：HuntingGame
@Date ：2023-02-07 19:22 
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        先算一下第一个链表的长度l1，和他最后一个节点e1。
        再算一下第二个链表的长度l2，和他最后一个节点e2。
        如果e1!=e2,那么他俩肯定不相交，不然e1肯定是等于e2的。
        如果e1 ==e2，那么先让链表1走l1-l2,然后俩链表一起走，一定会到相交节点。
        :param headA:
        :param headB:
        :return:
        """
        if headA is None and headB is None:
            return None
        cur1 = headA
        cur2 = headB
        n = 0
        while cur1.next:
            n +=1
            cur1 = cur1.next
        while cur2.next:
            n -=1
            cur2 = cur2.next
        if cur1 !=cur2:
            return None
        cur1 = headA if n > 0 else headB#交换长短链表，cur1指向长的
        cur2 = headB if cur1 == headA else headA
        n = abs(n)
        while n !=0:
            n -=1
            cur1 = cur1.next
        while cur1 !=cur2:
            cur1 = cur1.next
            cur2 =cur2.next

        return cur1
