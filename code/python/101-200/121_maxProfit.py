# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/27 9:29
# @File ：121_maxProfit.py
# @IDE ：PyCharm
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化利润为 0
        profit, min_price = 0, inf
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


s = Solution()
print(s.maxProfit([2, 1, 4]))
