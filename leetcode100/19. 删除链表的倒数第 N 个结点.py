#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：19. 删除链表的倒数第 N 个结点.py
@Author ：HuntingGame
@Date ：2023-02-01 20:42 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        pre = None
        enough = False
        while cur !=None:
            n-=1
            if n <=0:
                if n == 0:
                    enough = True # 说明够，链表的长度有那么多
                elif n == -1:
                    pre = head# 指向头结点，也就是当cur来到了节点最后的位置的时候，pre到了倒数n+1的位置
                else:
                    pre = pre.next
            cur = cur.next

        if not enough:
            #没有那么多个，那就不删嘛，返回头结点
            return head
        if pre == None:
            # 说明长度够，正好是头结点
            return head.next

        pre.next = pre.next.next #删除第n个节点
        return head

