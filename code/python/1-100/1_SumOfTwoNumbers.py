# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/14 22:23
# @File ：FirstSumOfTwoNumbers.py
# @IDE ：PyCharm
from typing import List


# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Lst = []
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    Lst.append(i)
                    Lst.append(y)
                    return Lst


s = Solution()
print(s.twoSum([3, 2, 4], 6))
