# -*- coding:utf-8 -*-
"""
file    : May03
author  : Alex Luo
desc    : $
date    : 2022-05-03 12:21
"""
# 最长字符串
"""
不含有重复字符的 最长子串 的长度
输入: s = "abcabcbb"
输出: 3 
"""
def long_str(s):
    # 双指针
    if len(set(s)) <= 2:
        return len(set(s))
    left, right = 0, 0
    max_length_str = 0
    while left <= len(s) - 1 or right <= len(s) - 1:
        if left == right:
            right += 1
        while right <= len(s) - 1 and s[right] not in s[left: right]:
            right += 1
        max_length_str = max_length_str if max_length_str > right - left else right - left
        left += 1
    return max_length_str

long_str('abcabcbb')

# s1 的排列之一是 s2 的 子串
"""
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba")

输入：s1= "ab" s2 = "eidboaoo"
输出：false
"""
def check_substring(s1, s2):
    def get_str_hashmap(s):
        hmp = {}
        for i in s:
            if i not in hmp:
                hmp[i] = 1
            else:
                hmp[i] += 1
        return hmp
    # s1比s2长，肯定不能被s2包含
    if len(s1) > len(s2):
        return False
    # 建立滑动窗口，左边为s1的起点，右边起点为s1的终点，共走len(s2) - len(s1)步
    left, right = 0, len(s1) - 1
    s1_hmp = get_str_hashmap(s1)
    while left <= len(s2) - len(s1):
        s2_hmp_tmp = get_str_hashmap(s2[left: right + 1])
        if s1_hmp == s2_hmp_tmp:
            return True
        else:
            left += 1
            right += 1
    return False
