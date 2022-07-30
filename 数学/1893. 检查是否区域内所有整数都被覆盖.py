# @Time : 2022-07-30 19:26
# @Author : Phalange
# @File : 1893. 检查是否区域内所有整数都被覆盖.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        zone = [0] * 52
        for each in ranges:
            zone[each[0]:each[1]+1] = [1] * (each[1] - each[0]+1)


        return (0 not in zone[left:right+1])

print(Solution().isCovered([[1,2],[3,4],[5,6]],2,5))
print(Solution().isCovered([[1,1]],50,50))