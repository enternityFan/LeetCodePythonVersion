# @Time : 2022-09-07 21:32
# @Author : Phalange
# @File : 1700. 无法吃午餐的学生数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mystack = collections.deque(sandwiches)
        myque = collections.deque(students)

        tmp = 0
        while mystack:
            if tmp == len(mystack) and mystack[0] !=myque[0]:
                break
            if myque[0] == mystack[0]:
                mystack.popleft()
                myque.popleft()
                tmp = 0
            else:
                val = myque.popleft()
                myque.append(val)
                tmp += 1

        return len(mystack)
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(Solution().countStudents(students,sandwiches))
