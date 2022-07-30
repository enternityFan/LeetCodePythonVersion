# @Time : 2022-07-29 14:58
# @Author : Phalange
# @File : 398. 随机数索引.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from collections import defaultdict
from typing import List
import random



"""
水塘抽样的方法
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i,num in enumerate(self.nums):
            if num == target:
                cnt +=1
                if random.randrange(cnt) == 0: # 1/k
                    ans = i
        return ans

"""
哈希表的方法
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)# 构建一个默认value为list的字典
        for i,num in enumerate(nums):
            self.pos[num].append(i)


    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])
