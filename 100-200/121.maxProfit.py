# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:22
# @Author  : xiname
# @File    : 121.maxProfit.py
# @IDE     : PyCharm
from cmath import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化利润为 0
        profit, min_price = 0, inf
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit