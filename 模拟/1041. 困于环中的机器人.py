# @Time : 2022-09-18 17:10
# @Author : Phalange
# @File : 1041. 困于环中的机器人.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        #存在环，就一定会回到（0，0）的位置
        """
        一轮执行结束后，方向与初始方向一致（向北），并且不是位于初始地点（0，0），那么将永远不会循环；否则，一定会产生循环（可以自行脑补一下，循环4次一定可以回到原点）。

作者：chu-jian-43
链接：https://leetcode.cn/problems/robot-bounded-in-circle/solution/by-chu-jian-43-vftv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param instructions:
        :return:
        """
        mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0 # 0是北，1是东，2是南，3是西
        pos = [0,0]
        for ins in instructions:
            if ins == "L":
                direction -= 1
            elif ins == "R":
                direction += 1

            else:
                pos[0] += mov[direction % 4][0]
                pos[1] += mov[direction % 4][1]
        if direction % 4 == 0 and (pos[0] or pos[1]):
            return False
        return True



