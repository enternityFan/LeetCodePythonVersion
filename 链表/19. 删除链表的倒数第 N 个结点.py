# @Time : 2022-09-09 13:37
# @Author : Phalange
# @File : 19. 删除链表的倒数第 N 个结点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针
        if not head or not head.next:
            return None
        fpt = head.next
        spt = head
        length = 2
        while fpt and fpt.next:
            spt = spt.next
            fpt = fpt.next.next
            if fpt !=None:
                length +=2
            else:
                length +=1

        if length % 2 == 0:
            cur = length // 2 - 1
        else:
            cur = length // 2
        if length == n :
            return head.next
        if (length - n-1) <=cur:
            spt = head
            cur = 0
        print(length - n)
        print(cur)
        while cur !=length - n-1:
            spt = spt.next
            cur +=1
        spt.next = spt.next.next

        return head
