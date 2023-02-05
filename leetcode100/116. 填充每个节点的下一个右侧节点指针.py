#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：116. 填充每个节点的下一个右侧节点指针.py
@Author ：HuntingGame
@Date ：2023-02-04 21:27 
C'est la vie!!! enjoy ur day :D
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def offer(self,cur):
        """
        向尾巴添加节点

        :param cur:
        :return:
        """
        self.size +=1
        print("In node:",cur.val)
        if not self.head:
            #头结点为空，那这个就是第一个节点
            self.head = cur
            self.tail = cur
        else:
            #说明之前有老尾巴
            self.tail.next = cur#变到老尾巴后面
            self.tail = cur#自己变成新尾巴

    def poll(self):
        """
        弹出头结点
        :return:
        """
        self.size -=1
        ans = self.head
        self.head = self.head.next
        ans.next = None #断连的操作。
        print("Out node:",ans.val)
        return ans
    def peek(self):
        print("peek node:",self.head.val)
class Solution:




    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        这个代码，只用了有限的几个变量，就把这个题给求解了
        :param root:
        :return:
        """
        if root is None:
            return root
        queue = MyQueue()
        queue.offer(root)
        while not queue.isEmpty():

            pre = None   # 上一个弹出的节点
            size = queue.size
            print("size :",size)
            queue.peek()
            #if size == 0:
                #break
            for i in range(size):
                print("i=",i)
                #print(queue.size)

                cur = queue.poll()
                if cur.left !=None:
                    queue.offer(cur.left)
                if cur.right !=None:
                    queue.offer(cur.right)

                if pre !=None:
                    pre.next = cur
                pre = cur

        return root


print(Solution().connect())
