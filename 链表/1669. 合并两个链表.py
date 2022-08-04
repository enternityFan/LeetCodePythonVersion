# @Time : 2022-08-04 17:17
# @Author : Phalange
# @File : 1669. 合并两个链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        cur1 = list1
        cur2 = list2
        prev1 = None

        # 找一下list2的尾节点
        t2 = list2
        while t2.next:
            t2 = t2.next



        idx = 0 #索引
        while cur1:
            if idx ==a:
                prev1.next = cur2

            elif idx == b+1:
                prev1.next = None# 到这里内存该回收删除的地方了
                t2.next = cur1

            prev1 = cur1
            cur1 = cur1.next
            idx +=1

        return list1