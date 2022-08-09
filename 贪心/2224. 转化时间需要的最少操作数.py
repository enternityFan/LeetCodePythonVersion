# @Time : 2022-08-09 17:26
# @Author : Phalange
# @File : 2224. 转化时间需要的最少操作数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        current = int(current[0])*60 + int( current[1])
        correct = correct.split(":")
        correct = int(correct[0])*60 + int(correct[1])
        ops = [60,15,5,1]
        err = correct - current
        times = 0
        idx = 0
        while err !=0:
            if err >=ops[idx]:
                err -=ops[idx]
                times +=1
            else:

                idx = idx +1 if idx !=3 else idx

        return times


current = "02:30"
correct = "04:35"
print(Solution().convertTime(current,correct))