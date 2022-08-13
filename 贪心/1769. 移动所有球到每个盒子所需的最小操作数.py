# @Time : 2022-08-13 16:25
# @Author : Phalange
# @File : 1769. 移动所有球到每个盒子所需的最小操作数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            if boxes[i] == "1":
                for j in range(n):
                    ans[j] +=abs(i-j)

        return ans

print(Solution().minOperations("110"))
