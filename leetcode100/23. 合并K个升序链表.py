#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：23. 合并K个升序链表.py
@Author ：HuntingGame
@Date ：2023-02-02 9:17 
C'est la vie!!! enjoy ur day :D
'''
import heapq
from typing import Optional, List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        小根堆。首先让头结点都放小根堆，然后弹出最小的，把这个头结点的下一个结点再放到小根堆里面，然后再弹出来。。。就是这个思路
        :param lists:
        :return:
        """
        myheap = []
        for i,each in enumerate(lists):
            if each is not None:
                heapq.heappush(myheap,(each.val,i))
        if len(myheap) == []:
            return None

        head = cur = ListNode(None)
        while myheap:
            val,idx = heapq.heappop(myheap)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx].next
            lists[idx] = lists[idx].next
            if node:
                heapq.heappush(myheap,(node.val,idx))

        return head.next

