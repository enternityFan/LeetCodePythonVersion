#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：148. 排序链表.py
@Author ：HuntingGame
@Date ：2023-02-06 16:27 
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        这里就是不用容器O(1)的空间复杂度做的。那就是用merge排序；其实merge排数组的话
        是做不到的，因为需要辅助数组，但是链表的话就可以了
        这里Merge的长度每次就是2,4,8,16...
        这个题很考验coding的，尤其是边界条件。
        #TODO

        :param head:
        :return:
        """
        N = 0
        cur = head
        while cur is not None:
            N+=1
            cur = cur.next
        h = head
        teamFirst = head
        pre = None
        length = 1#其实就意味着长度为二。
        while length < N:
            while teamFirst is not None:
                hthtn = self.hthtn(teamFirst,length)
                mhmt = self.merge(hthtn[0],hthtn[1],hthtn[2],hthtn[3])
                if h == teamFirst:
                    h = mhmt[0]
                    pre = mhmt[1]
                else:
                    pre.next = mhmt[0]
                    pre = mhmt[1]

                teamFirst = hthtn[4]





            length <<=1

    def hthtn(self,teamFirst,length):
        """
        返回5个变量：左组的头尾，右组的头尾，下一作的next
        :param teamFirst:
        :param length:
        :return:
        """
        pass


    def merge(self,ls,le,rs,re):
        if rs == None:
            return []























