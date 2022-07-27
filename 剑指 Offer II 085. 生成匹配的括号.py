# @Time : 2022-03-02 17:35
# @Author : Phalange
# @File : 剑指 Offer II 085. 生成匹配的括号.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S,left,right):
            if len(S) == 2 * n:
                res.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S,left+1,right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S,left,right+1)
                S.pop()
        backtrack([],0,0)
        return res


S = Solution()
S.generateParenthesis(3)