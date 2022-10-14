# @Time : 2022-10-14 8:32
# @Author : Phalange
# @File : 367. 有效的完全平方数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <=r:
            mid = l + ((r - l) >> 1)
            if num % mid == 0 and num // mid == mid:
                return True
            elif num < mid ** 2:
                r = mid - 1
            else:
                l = mid + 1

        return False