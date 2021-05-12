def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def heap_insert(arr, index):
    father_idx = int((index - 1) / 2)
    while arr[index] > arr[father_idx]:
        swap(arr, index, father_idx)
        index = father_idx
        father_idx = int((index - 1) / 2)

def find_max(arr, i, j):
    if arr[i] > arr[j]:
        return i
    else:
        return j

def heapify(arr, index, heap_size):
    while 2 * index + 1 < heap_size:
        left_son = 2 * index + 1
        right_son = 2 * index + 2
        if right_son >= heap_size:
            max_index = left_son
        else:
            max_index = find_max(arr, left_son, right_son)
        if arr[max_index] > arr[index]:
            swap(arr, max_index, index)
            index = max_index
        else:
            break


def heap_sort(arr):
    if len(arr) < 2:
        return arr
    heap_size = 1
    for index in range(1, len(arr)):
        heap_insert(arr, index)
        heap_size += 1
    swap(arr, 0, heap_size-1)
    heap_size -= 1
    index = 0
    while heap_size > 0:
        heapify(arr, index, heap_size)
        swap(arr, index, heap_size-1)
        heap_size -= 1
    return

if __name__ == '__main__':
    arr = [5, 6, 4, 2, 7, 8, 1, 9, 3, 2]
    heap_sort(arr)
    print(arr)