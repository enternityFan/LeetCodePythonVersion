# @Time : 2022-07-29 11:29
# @Author : Phalange
# @File : 412. Fizz Buzz.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if (i+1) %3 == 0 and (i+1) % 5 == 0:
                res.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                res.append("Fizz")
            elif (i + 1) % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i+1))

        return res