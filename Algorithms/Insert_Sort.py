# 插入排序
# 提取每一个元素，放到大数的左边。
# 一个for循环
# 如果a[n]比a[n+1]大，交换两数，反之则a[n+1]=a[n]
# 相比冒泡循环，效率提升

import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1 # j 是 arr[i] 的前一个元素
        while j >= 0 and key < arr[j]: # 后一个元素比前一个元素小 (找到)
            arr[j + 1] = arr[j] # 后一个元素等于前一个元素 （交换位置）
            j -= 1
        arr[j + 1] = key

