#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 19:59
# @Author  : HuntingGame
# @FileName: 1603. 设计停车系统.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D



class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.num = {1:big,2:medium,3:small}


    def addCar(self, carType: int) -> bool:
        if self.num[carType] >0:
            self.num[carType] -=1
            return True
        else:
            return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
