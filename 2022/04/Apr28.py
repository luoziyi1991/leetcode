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


# 轮转数组
"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
"""


def rotate_arr(nums, k):
    k %= len(nums)

    def reverse(x, l, r):
        while l <= r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1
        return x

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums
