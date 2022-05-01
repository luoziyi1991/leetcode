# -*- coding:utf-8 -*-
"""
file    : May01
author  : Alex Luo
desc    : https://leetcode-cn.com/problems/reverse-string/
date    : 2022-05-01 14:08
"""
# 反转字符串
"""
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
"""


def reverse_string(s):
    left, right = 0, len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


# 反转字符串中得单词
"""
输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
"""


def word_in_string(s):
    return ' '.join(word[::-1] for word in s.split(' '))


# 链表节点
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""快慢指针
给定一个头结点为 head 的非空单链表，返回链表的中间结点。 
"""


def get_middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


# 删除链表得第N个节点
def remove_n_node(head, n):
    res_node = head
    fst, sec = head, head
    for i in range(n):
        fst = fst.next
    if not fst:
        return head.next
    while fst.next:
        fst = fst.next
        sec = sec.next
    sec.next = sec.next.next
    return res_node
