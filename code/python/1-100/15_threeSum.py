# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/23 13:37
# @File ：15_threeSum.py
# @IDE ：PyCharm
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
# 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
# 请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对数组排序
        nums.sort()
        new_nums = []
        # 特例
        if len(nums) < 3 or nums is None:
            return []
        for k in range(len(nums) - 1):
            # 结束条件
            if nums[k] > 0:
                break
            i, j = k + 1, len(nums) - 1
            while True:
                if i == j:
                    break
                sum_nums = nums[k] + nums[i] + nums[j]
                if sum_nums == 0:
                    temp_nums = [nums[k], nums[i], nums[j]]  # 注意顺序，用来判断是否重复的解
                    # print("k,i,j,temp_nums:",k,i,j,temp_nums)
                    if temp_nums not in new_nums:
                        new_nums.append(temp_nums)
                    i += 1
                # 移动指针
                elif sum_nums > 0:
                    j -= 1
                elif sum_nums < 0:
                    i += 1
        return list(new_nums)


s = Solution()
# print(s.threeSum([0, 0, 0]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
