# @Time : 2022-10-14 12:46
# @Author : Phalange
# @File : 386. 字典序排数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1,n+1)),key=lambda x:str(x))


print(Solution().lexicalOrder(140))