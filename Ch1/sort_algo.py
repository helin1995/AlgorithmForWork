# coding: utf-8

class SortAlg():
    def swap(self, arr, i, j):
        '''
        交换数组arr中i位置和j位置元素的值
        :param arr:
        :param i:
        :param j:
        :return:
        '''
        # temp = arr[i]
        # arr[i] = arr[j]
        # arr[j] = temp

        # 利用异或运算交换两个变量的值
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]

    def selection_sort(self, arr):
        '''
        选择排序
        :param arr:
        :return: 排序后的数组
        '''
        if len(arr) < 2:
            return arr

        for epoch in range(len(arr)-1):
            min_val_index = epoch
            # 找到本轮次的最小值所在的位置（下标）
            for n in range(epoch+1, len(arr)):
                if arr[n] < arr[min_val_index]:
                    min_val_index = n
            # 将最小值和第epoch个元素交换位置
            self.swap(arr, epoch, min_val_index)
        return arr

    def bubble_sort(self, arr):
        '''
        冒泡排序
        :param arr:
        :return:
        '''
        if len(arr) < 2:
            return arr

        for max_iter in range(len(arr), 0, -1):
            for n in range(max_iter-1):
                if arr[n] > arr[n+1]:
                    self.swap(arr, n, n+1)
        return arr

    def insert_sort(self, arr):
        '''
        插入排序
        :param arr:
        :return:
        '''
        if len(arr) < 2:
            return arr

        for n in range(1, len(arr)):
            curr = n  # 当前的数
            while curr > 0:
                # 如果有序，则无需操作
                if arr[curr] >= arr[curr-1]:
                    break
                # 如果无序，则交换当前的数和前一个数，并且当前的数变为前一个数
                else:
                    self.swap(arr, curr-1, curr)
                    curr -= 1
        return arr
