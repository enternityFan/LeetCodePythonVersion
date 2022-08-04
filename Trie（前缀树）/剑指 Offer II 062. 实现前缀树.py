# @Time : 2022-08-04 9:54
# @Author : Phalange
# @File : 剑指 Offer II 062. 实现前缀树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Node:
    def __init__(self):
        self.nexts = [None]*26
        self.passed = 0
        self.ends = 0


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        cur_node.passed +=1

        for c in word:
            # 1.首先判断是否当前存在这个路
            path = ord(c) - ord('a')
            if cur_node.nexts[path] == None:# 不存在这条路
                cur_node.nexts[path] = Node() # 新建一个节点咯
            cur_node = cur_node.nexts[path]
            cur_node.passed +=1
        cur_node.ends +=1










    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nodes = self.root
        for c in word:
            path = ord(c) - ord('a')
            if nodes.nexts[path] == None:
                return False
            nodes = nodes.nexts[path]
        if nodes.ends ==0:
            return False
        return True



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nodes = self.root
        for c in prefix:
            path = ord(c) - ord('a')
            if nodes.nexts[path] == None:
                return False
            nodes = nodes.nexts[path]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)