# @Time : 2022-07-29 15:23
# @Author : Phalange
# @File : 382. 链表随机节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode
import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head


    def getRandom(self) -> int:
        node,i,ans = self.head,1,0
        while node:
            if random.randrange(i) == 0:
                ans = node.val
            i+=1
            node = node.next


        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()