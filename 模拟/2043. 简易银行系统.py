#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 21:05
# @Author  : HuntingGame
# @FileName: 2043. 简易银行系统.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account2 <= self.n and account1 <= self.n and account1 >=1 and account2 >=1 and self.balance[account1-1] - money >=0 :
            self.balance[account1-1] -=money
            self.balance[account2-1] +=money
            return True
        return False



    def deposit(self, account: int, money: int) -> bool:
        if account >=1 and account <=self.n:
            self.balance[account-1] +=money
            return True
        return False


    def withdraw(self, account: int, money: int) -> bool:
        if account >=1 and account <=self.n and self.balance[account -1] - money >=0:
            self.balance[account-1] -=money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
