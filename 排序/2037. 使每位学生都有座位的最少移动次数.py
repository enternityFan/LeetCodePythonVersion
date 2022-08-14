# @Time : 2022-08-14 16:08
# @Author : Phalange
# @File : 2037. 使每位学生都有座位的最少移动次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        ans = 0
        for i in range(n):
            ans+=abs(students[i] - seats[i])

        return ans