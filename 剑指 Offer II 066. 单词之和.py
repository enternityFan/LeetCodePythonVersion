# @Time : 2022-07-29 21:31
# @Author : Phalange
# @File : 剑指 Offer II 066. 单词之和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

import collections

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mydict = collections.defaultdict(int)


    def insert(self, key: str, val: int) -> None:
        self.mydict[key] = val


    def sum(self, prefix: str) -> int:
        count = 0
        for k,v in self.mydict.items():
            if prefix == k[:len(prefix)]:
                count +=v



        return count



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)