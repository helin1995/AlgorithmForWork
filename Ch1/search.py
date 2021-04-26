# coding: utf-8

def binary_search(arr, elem):
    '''
    二分查找
    :param arr: 有序数组
    :param elem: 需要查找的元素
    :return: 返回元素对应的下标
    '''
    low  = 0
    high = len(arr) - 1
    while low <= high:
        # 求[low, high]中点的方法1：
        # mid = low + int((high - low) / 2)
        # 求[low, high]中点的方法2：
        mid = low + ((high - low) >> 1)
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None