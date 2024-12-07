# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:10
# @Author  : xiname
# @File    : 1.twoSum.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Lst = []
        for i in range(len(nums)):
            for y in range(i+1, len(nums)):
                if nums[i] + nums[y] == target:
                    Lst.append(i)
                    Lst.append(y)
                    return Lst