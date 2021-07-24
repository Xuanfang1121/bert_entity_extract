# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 22:50
# @Author  : zxf
arr = [1, 3, 2, 1, 5]
n = len(arr)
s = [0]
for val in arr:
    print("s", s)
    print(s[-1] ^ val)
    s.append(s[-1] ^ val)

print("final s: ", s)