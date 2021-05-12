def get_digits(num):
    res = 0
    while num != 0:
        num //= 10
        res += 1
    return res

def get_num_digit(num, idx):
    return (num // (10 ** idx)) % 10

def bucket_sort(arr):
    if len(arr) < 2:
        return arr
    max_num = max(arr)  # 找到arr中最大的数
    digits = get_digits(max_num)  # 找到最大的数是多少位的
    buckets = [[] for i in range(10)]
    for i in range(digits):
        # 入桶
        for num in arr:
            digit = get_num_digit(num, i)
            buckets[digit].append(num)
        # 出桶
        index = 0
        for bucket in buckets:
            if len(bucket) == 0:
                continue
            else:
                for num in bucket:
                    arr[index] = num
                    index += 1
        buckets = [[] for i in range(10)]

if __name__ == '__main__':
    arr = [17, 13, 25, 100, 72, 45, 78, 21]
    bucket_sort(arr)
    print(arr)