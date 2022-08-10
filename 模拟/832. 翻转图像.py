# @Time : 2022-08-10 21:29
# @Author : Phalange
# @File : 832. 翻转图像.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(n):
                image[i][j] = 0 if image[i][j] == 1 else 1

        return image