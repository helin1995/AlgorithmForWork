# coding: utf-8

# coding: utf-8
# 归并排序

def merge(left_sort, right_sort):
    result = []
    l_id = r_id = 0
    while (l_id < len(left_sort)) and (r_id < len(right_sort)):
        if left_sort[l_id] <= right_sort[r_id]:
            result.append(left_sort[l_id])
            l_id += 1
        else:
            result.append(right_sort[r_id])
            r_id += 1
    if l_id == len(left_sort):
        result += right_sort[r_id:]
    else:
        result += left_sort[l_id:]
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) >> 1
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # print(left, right)
    return merge(left, right)


if __name__ == '__main__':
    arr = [5, 2, 6, 1, 3, 8, 7, 4, 9, 10]

    res = merge_sort(arr)
    print('排序后的结果: ', res)
