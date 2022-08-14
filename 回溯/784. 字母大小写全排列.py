# @Time : 2022-08-14 14:00
# @Author : Phalange
# @File : 784. 字母大小写全排列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        tmp = []
        def process(idx):
            if idx == len(s):
                strs = "".join(tmp)
                if strs not in ans:
                    ans.append(strs)
                return
            if s[idx] not in "123456789":
                process(idx+1)
                if tmp[idx] >="a" and tmp[idx] <="z":
                    tmp[idx] = tmp[idx].upper()
                    process(idx+1)
                    tmp[idx] = tmp[idx].lower()
                else:
                    tmp[idx] = tmp[idx].lower()
                    process(idx+1)
                    tmp[idx] = tmp[idx].upper()
            else:
                process(idx+1)
        tmp = [i for i in s]
        process(0)
        return ans

print(Solution().letterCasePermutation("a1b2"))
