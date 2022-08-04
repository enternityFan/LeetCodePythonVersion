# @Time : 2022-08-04 19:25
# @Author : Phalange
# @File : 14. 最长公共前缀.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minlen = len(min(strs, key=lambda x: len(x)))
        ans = ""
        for i in range(minlen):
            tmp = strs[0][i]
            for each in strs:
                if tmp != each[i]:
                    return ans
            ans += tmp

        return ans

print(Solution().longestCommonPrefix(["fly","flow","flight"]))
