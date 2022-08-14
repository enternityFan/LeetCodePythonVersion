# @Time : 2022-08-14 15:51
# @Author : Phalange
# @File : 876. 链表的中间结点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast == None:
            return slow

        return slow.next