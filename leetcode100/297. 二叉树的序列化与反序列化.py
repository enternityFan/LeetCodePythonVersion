#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：297. 二叉树的序列化与反序列化.py
@Author ：HuntingGame
@Date ：2023-02-09 10:51 
C'est la vie!!! enjoy ur day :D
'''
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        print("========Serialize==================")
        ans = collections.deque()
        if root is None:
            print("here")
            ans.append(None)
        else:
            ans.append(str(root.val))
            myqueue = collections.deque()
            myqueue.append(root)
            while len(myqueue) != 0:
                root = myqueue.popleft()
                if root.left:
                    ans.append(str(root.left.val))
                    myqueue.append(root.left)
                else:
                    ans.append(None)
                if root.right:
                    ans.append(str(root.right.val))
                    myqueue.append(root.right)
                else:
                    ans.append(None)
        print(ans)
        while len(ans) != 0 and ans[-1] == None:
            print(ans[-1])
            ans.pop()
        tmp = "["
        str1 = ans.popleft() if len(ans) != 0 else None
        tmp += "null" if str1 == None else str(str1)
        while len(ans) != 0:
            str1 = ans.popleft()
            tmp += ","
            tmp += "null" if str1 == None else str(str1)
        tmp += "]"
        print(tmp)
        return tmp

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        strs = data[1:-1].split(",")  # 去掉左右括号。
        idx = 0
        root = self.generateNode(strs[idx])
        idx += 1
        myqueue = collections.deque()
        if root:
            myqueue.append(root)

        node = None
        print("===========================")
        while myqueue:
            node = myqueue.popleft()
            print(node.val)
            # 下面的专门的判断是为了去除最后的空，所以越界了就默认为空。
            print("nodel.left=", "null" if idx == len(strs) else strs[idx])
            node.left = self.generateNode("null" if idx == len(strs) else strs[idx])
            idx = len(strs) if idx == len(strs) else idx + 1
            print("nodel.right=", "null" if idx == len(strs) else strs[idx])
            node.right = self.generateNode("null" if idx == len(strs) else strs[idx])
            idx = len(strs) if idx == len(strs) else idx + 1
            if node.left is not None:
                myqueue.append(node.left)
            if node.right is not None:
                myqueue.append(node.right)

        return root

    def generateNode(self, val):
        if val == "null":
            return None
        return TreeNode(int(val))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))