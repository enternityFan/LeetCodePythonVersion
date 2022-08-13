# @Time : 2022-08-13 16:08
# @Author : Phalange
# @File : 面试题 08.07. 无重复字符串的排列组合.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        tmp = []
        def process(idx):
            if idx == len(S):
                ans.append("".join(tmp[:]))
                return

            # 认为，i之前的，都排好序了
            for i in range(idx,len(S)):
                tmp[i], tmp[idx] = tmp[idx], tmp[i]
                process(idx + 1)
                tmp[i], tmp[idx] = tmp[idx], tmp[i]
        tmp = list(S)
        process(0)
        return ans

print(Solution().permutation("qwe"))
print(Solution().permutation("ab"))