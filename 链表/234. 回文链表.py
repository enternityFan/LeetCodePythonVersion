# @Time : 2022-08-04 17:39
# @Author : Phalange
# @File : 234. 回文链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 第一步，找中点
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 第二步，反转一下链表后部分

        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 第三步，开始判断是否回文
        flag = True # 默认为True
        cur1 = head
        cur2 = prev
        while cur1 and cur2 !=cur1:
            if cur1.val !=cur2.val:
                flag = False
                break
            cur1 = cur1.next
            cur2 = cur2.next

        # 第四步，复原链表
        cur = prev
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp


        return flag



