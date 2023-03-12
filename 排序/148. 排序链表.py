#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：148. 排序链表.py
@Author ：HuntingGame
@Date ：2023-03-12 12:53 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            fast,slow = fast.next.next,slow.next
        mid,slow.next = slow.next,None #mid是奇数长度的中点，偶数长度的上中点；然后在这里断开
        # 开始递归的排序两侧
        left,right = self.sortList(head),self.sortList(mid)
        # 合并左右链表，然后返回
        h = res = ListNode(0)#建立一个辅助头
        while left and right:
            if left.val < right.val:
                h.next,left = left,left.next
            else:
                h.next,right = right,right.next
            h = h.next
        h.next = left if left else right
        return res.next