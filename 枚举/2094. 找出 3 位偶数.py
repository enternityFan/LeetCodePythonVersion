# @Time : 2022-09-14 21:47
# @Author : Phalange
# @File : 2094. 找出 3 位偶数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        even =[]
        for i in range(n):
            if digits[i] % 2 == 0:
                even.append(i)
        for i in range(n):
            if digits[i] == 0 :
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in even:
                    if j ==k or i == k:
                        continue

                    ans.add(digits[i]*100 + digits[j]*10 + digits[k])

        ans = list(ans)
        ans.sort()
        return ans

print(Solution().findEvenNumbers([2,1,3,0]))