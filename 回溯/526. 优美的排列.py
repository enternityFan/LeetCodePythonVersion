# @Time : 2022-09-08 14:31
# @Author : Phalange
# @File : 526. 优美的排列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []

    def countArrangement(self, n: int) -> int:

        def process(record,idx, curEnd):
            if idx == curEnd+1:
                self.ans.append(self.tmp[:])
                return


            for i in range(1,curEnd+1):
                if i not in record:

                    if i % idx == 0 or idx % i == 0:
                        self.tmp.append(i)
                        record.add(i)
                        process(record,idx+1,curEnd)
                        self.tmp.pop()
                        record.remove(i)

        record = set()
        process( record,1, n)
        return len(self.ans)

print(Solution().countArrangement(4))
