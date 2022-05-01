# -*- coding:utf-8 -*-
"""
file    : Apr29
author  : Alex Luo
desc    : $
date    : 2022-04-29 18:55
"""
# 快慢指针
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
初始时刻：[0, 1, 0, 3, 12]，左指针指向首位，因为此时已处理序列为空，尾部即为首位；右指针指向首位，因为此时待处理序列为原数组，头部即为首位
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


def move_zeros(nums):
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums


# 非递减数组两数和
"""
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
"""


def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
