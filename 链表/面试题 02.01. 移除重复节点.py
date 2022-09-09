# @Time : 2022-09-09 14:00
# @Author : Phalange
# @File : 面试题 02.01. 移除重复节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        record = set()
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            if cur.val not in record:
                record.add(cur.val)
                prev = cur
            else:
                prev.next = cur.next

            cur = cur.next

        return head





