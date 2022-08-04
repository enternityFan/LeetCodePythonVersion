# @Time : 2022-08-04 12:58
# @Author : Phalange
# @File : 1051. 高度检查器.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        计数排序
        :param heights:
        :return:
        """
        m = max(heights)
        cnt = [0] * (m+1)

        for each in heights:
            cnt[each] +=1

        idx = ans = 0
        for i in range(1,m + 1):
            for j in range(cnt[i]):
                if heights[idx] !=i:
                    ans +=1
                idx +=1
        return ans

print(Solution().heightChecker([1,1,4,2,1,3]))