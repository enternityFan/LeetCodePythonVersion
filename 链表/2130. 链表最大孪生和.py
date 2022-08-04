# @Time : 2022-08-04 16:42
# @Author : Phalange
# @File : 2130. 链表最大孪生和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #way1 使用数组
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        maxValue = -100000
        n = len(arr)
        for i in range(n//2):
            maxValue = max(maxValue,arr[i] + arr[n-1-i])
        return maxValue



class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #way2 使用栈,快慢指针
        arr = []
        cur = head

        pt1 = cur
        pt2 = cur.next

        while pt2.next and pt2.next.next:
            pt1 = pt1.next
            pt2 = pt2.next.next
        # pt1指向n//2的位置
        mid = pt1
        cur = pt1.next
        while cur:
            arr.append(cur.val)
            cur = cur.next
        maxValue = -10000
        cur = head
        while cur != mid.next:
            maxValue = max(maxValue,cur.val + arr.pop())
            cur = cur.next
        return maxValue



class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # way3 空间O(1)
        fast = head
        slow = head
        # 1.找链表上中点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2.反转链表后半链表
        cur = slow
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 3.计算孪生和
        maxValue = -1000
        cur = head
        tail = prev
        while cur and prev:
            maxValue = max(maxValue,cur.val + prev.val)
            cur = cur.next
            prev = prev.next
        # 4.重新反转回来
        cur = tail
        prev = None
        while cur != slow:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return maxValue