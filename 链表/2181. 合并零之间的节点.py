# @Time : 2022-08-04 16:28
# @Author : Phalange
# @File : 2181. 合并零之间的节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        newHead = ListNode()
        cur2 = newHead

        zone = 0 #计算这个小区间内的求和的值
        flag = 0 # 记录是不是第一个区间
        while cur:
            if cur.val ==0:
                if flag == 0:
                    flag = 1
                    cur = cur.next
                    continue#不执行下面的
                cur2.val = zone
                if cur.next !=None:
                    cur2.next = ListNode()
                    cur2 = cur2.next
                else:
                    break
                zone = 0
            else:
                zone +=cur.val

            cur = cur.next

        return newHead



