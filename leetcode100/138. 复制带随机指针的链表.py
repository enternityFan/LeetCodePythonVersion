#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：138. 复制带随机指针的链表.py
@Author ：HuntingGame
@Date ：2023-02-06 10:01 
C'est la vie!!! enjoy ur day :D
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        哈希表做很简单
        遍历一遍，key是老节点，value是新节点，
        然后接下来遍历这个map，a的next和random就是通过查a的map知道的。
        下面的代码的话把做表这个环节省去了
        :param head:
        :return:
        """
        if not head:
            return None
        cur = head
        next = None
        #下面这个while的操作
        # 1-> 2 -> 3 ->None
        # 1-> 1' -> 2 -> 2'
        while cur !=None:
            cur.next = Node(cur.val)
            cur.next.next = next
            cur = next

        cur = head
        copy = None
        # 1 1' 2 2' 3 3'
        #下面是在依次设置1' 2' 3'的random指针
        while cur !=None:
            next = cur.next.next
            copy = cur.next
            copy.random = cur.random.next if cur.random !=None else None
            cur = next

        res = head.next
        cur = head
        # 新，老混在一起，next方向上，random正确
        # next方向上新老链表分离
        while cur !=None:
            next = cur.next.next
            copy = cur.next
            cur.next = next
            copy.next = next.next if next !=None else None
            cur = next
        return res