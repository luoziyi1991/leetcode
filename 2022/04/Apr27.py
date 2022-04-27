#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Apr27.py
# @Author: luoziyi
# @Date  : 2022/4/26
# @Desc  : 题目网址 https://leetcode-cn.com/study-plan/algorithms/?progress=up7j1mi

# 二分查找01
"""
n个元素的升序数组nums，查找x，找到返回索引，没找到返回-1
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
"""


def search_01(nums, x):
    # 双指针
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if x == nums[mid]:
            return mid
        elif x > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 二分查找002
"""
第一个错误版本；
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致出错的第一个错误的版本。你可以通过调用isBadVersion(version)判断是否出错
"""


def isBadVersion(x):
    # 判断是否是错误版本
    return 0


def first_bad_version(n):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) >> 1
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left
