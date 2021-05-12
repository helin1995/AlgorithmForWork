
def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def quick_sort(arr, L, R):
    if L < R:
        lp = L - 1
        rp = R + 1
        p = L
        last = arr[R]
        while p < rp:
            if arr[p] < last:
                swap(arr, p, lp+1)
                lp += 1
                p += 1
            elif arr[p] == last:
                p += 1
            else:
                swap(arr, p, rp-1)
                rp -= 1

        quick_sort(arr, 0, lp)
        quick_sort(arr, rp, R)


if __name__ == '__main__':
    arr = [5, 2, 6, 1, 3, 8, 7, 4, 9, 10, 5]

    quick_sort(arr, 0, len(arr)-1)
    print('排序后的结果: ', arr)