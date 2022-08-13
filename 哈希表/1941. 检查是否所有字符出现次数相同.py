# @Time : 2022-08-13 17:29
# @Author : Phalange
# @File : 1941. 检查是否所有字符出现次数相同.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

class BitMap:
    def __init__(self,maxValue):
        self.bits = (maxValue + 32) >> 5

    def add(self,num):
        self.bits[num >> 5] |=(1 << (num & 31))

    def delete(self,num):
        self.bits[num >> 5] &=~(1 << (num & 31))

    def contains(self,num):
        return (self.bits[num >> 5] & (1 << (num &31))) !=0

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # 使用位图来做
        nums = [0]*26

        for c in s:
            nums[ord(c) - ord('a')] +=1
        prev = None
        for each in nums:
            if each !=0:
                if prev == None:
                    prev = each
                elif prev != each:
                    return False
        return True

print(Solution().areOccurrencesEqual("abcabc"))