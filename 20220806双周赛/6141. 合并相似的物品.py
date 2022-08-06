# @Time : 2022-08-06 22:30
# @Author : Phalange
# @File : 6141. 合并相似的物品.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        mydict = collections.defaultdict(int)
        for each in items1:
            mydict[each[0]] +=each[1]

        for each in items2:
            mydict[each[0]] +=each[1]
        ans = [list(each) for each in sorted(mydict.items(),key=lambda x:x[0])]
        return ans



items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(Solution().mergeSimilarItems(items1,items2))