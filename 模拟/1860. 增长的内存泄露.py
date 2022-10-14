# @Time : 2022-10-14 12:18
# @Author : Phalange
# @File : 1860. 增长的内存泄露.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:


        cnt = 1
        flag = 0



        while memory1 >= cnt or memory2 >=cnt:
            if memory2 > memory1:
                memory2 -=cnt
            else:
                memory1 -=cnt


            cnt +=1


        return [cnt,memory1,memory2]


print(Solution().memLeak(8,11))