# @Time : 2022-07-29 8:13
# @Author : Phalange
# @File : 66. 加一.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if digits[-1] + 1 < 10:
            digits[-1]  +=1

        else:
            flag = 1 # 表示进位
            idx = length - 1 # 表示当前位置
            while idx != -1:
                if flag == 1:
                    digits[idx] = 0

                    idx -=1
                    if idx != -1:
                        digits[idx] +=1
                        flag = 1 if digits[idx] == 10 else 0
                else:
                    break
            if flag == 1:
                digits[0] = 0
                digits.insert(0,1)

        return digits




        # way2
        # digits = [str(i) for i in digits]
        # mystr = "".join(digits)
        # myint = int(mystr) + 1
        # return [int(each) for each in str(myint)]



s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([8,9,9]))