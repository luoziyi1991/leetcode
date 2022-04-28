# -*- coding:utf-8 -*-
"""
file    : Apr28
author  : Alex Luo
desc    : https://leetcode-cn.com/study-plan/algorithms/?progress=uma1x7e
date    : 2022-04-28 10:54
"""
# 双指针01
"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
要求空间复杂度O(n)
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
"""


def sorted_list_squares(nums):
    res = [0] * len(nums)
    # 利用有序的特性，选择双指针
    left, right, cur = 0, len(nums) - 1, len(nums) - 1
    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            res[cur] = nums[left] * nums[left]
            left += 1
        else:
            res[cur] = nums[right] * nums[right]
            right -= 1
        cur -= 1
    return res
