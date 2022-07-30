# @Time : 2022-07-28 8:01
# @Author : Phalange
# @File : 1331. 数组序号转换.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr = list(enumerate(arr))
        arr.sort(key=lambda x:x[1])
        res = [0] * len(arr)
        prev = None
        idx = 0
        for each in arr:
            if prev != each[1]:
                idx +=1

            res[each[0]] = idx
            prev = each[1]

        return res




s = Solution()

print(s.arrayRankTransform([40,10,20,30]))
print(s.arrayRankTransform([10,10,20,30]))