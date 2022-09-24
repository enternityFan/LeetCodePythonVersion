# @Time : 2022-09-24 13:43
# @Author : Phalange
# @File : 1652. 拆炸弹.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if k == 0:
            return [0] * len(code)
        if k > 0:
            for i in range(len(code)):
                tmp = 0
                j = 0
                while j < k:
                    if i+j+1 < len(code):
                        tmp +=code[i+j+1]
                    else:
                        tmp +=code[i+j+1-len(code)]
                    j +=1
                ans.append(tmp)
        else:
            for i in range(len(code)):
                tmp = 0
                j = 0
                while j < abs(k):
                    if i-j-1 <0:
                        tmp +=code[len(code)+i-j-1]
                    else:
                        tmp +=code[i-j-1]
                    j+=1
                ans.append(tmp)


        return ans
code = [2,4,9,3]
k = -2
print(Solution().decrypt(code,k))



