# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:16
# @Author  : xiname
# @File    : 26.removeDuplicates.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
        nums[:len(new_list)] = new_list
        return len(new_list)