#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：328. 奇偶链表.py
@Author ：HuntingGame
@Date ：2023-02-09 19:36 
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstOdd = None
        firstEven = None
        odd = None
        even = None
        nextNode = None
        cnt = 1
        while head:
            nextNode = head.next
            head.next = None
            if (cnt & 1) == 1:
                #奇序号
                firstOdd = head if not firstOdd else firstOdd
                if odd:
                    odd.next = head
                odd = head
            else:
                firstEven = head if not firstEven else firstEven
                if even:
                    even.next = head
                even = head
            cnt +=1
            head = nextNode
        if odd:
            odd.next = firstEven

        return firstOdd if firstOdd else firstEven