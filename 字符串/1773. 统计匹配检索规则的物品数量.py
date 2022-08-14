# @Time : 2022-08-14 12:28
# @Author : Phalange
# @File : 1773. 统计匹配检索规则的物品数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n = len(items)
        ans = 0
        mymap = {"type":0,"color":1,"name":2}
        for i in range(n):
            if items[i][mymap[ruleKey]] == ruleValue:
                ans +=1
        return ans