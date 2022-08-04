# @Time : 2022-08-04 17:03
# @Author : Phalange
# @File : 1290. 二进制链表转整数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        idx = 0
        ans = 0
        while arr:
            ans +=arr.pop()* (2 ** idx)
            idx +=1
        return ans
