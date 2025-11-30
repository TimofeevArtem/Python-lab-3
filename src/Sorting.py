def bubble_sort(arr: list[int]):
    """Функция сортировки пузырьком"""
    for j in range(len(arr)):
        for elem in range(len(arr) - 1):
            if arr[elem] > arr[elem + 1]:
                arr[elem], arr[elem + 1] = arr[elem + 1], arr[elem]
    return arr

def quick_sort(arr: list[int]):
    """Функция быстрой сортировки"""
    last_elem = len(arr) - 1
    left = []
    right = []
    if len(arr) <= 1:
        return arr
    for i in range(len(arr) - 1):
        if arr[i] <= arr[last_elem]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [arr[last_elem]] + quick_sort(right)

def count_sort(arr: list[int]):
    """Функция сортировки подсчетом"""
    if arr:
        mn = min(arr)
        count_arr = [0] * (max(arr) - min(arr) + 1)
        for i in arr:
            count_arr[i - mn] += 1
        arr = []
        for i in range(len(count_arr)):
            arr += [i + mn] * count_arr[i]
        return arr
    else:
        return arr


def radix_sort(arr: list[int]):
    """Функция radix сортировки"""
    neg_arr = []
    pos_arr = []
    sort_list_pos = []
    sort_list_neg = []
    max_len_neg = 0
    max_len_pos = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            neg_arr.append(abs(arr[i]))
            if len(str(arr[i])) > max_len_neg:
                max_len_neg = len(str(arr[i])) - 1
        else:
            pos_arr.append(arr[i])
            if len(str(arr[i])) > max_len_pos:
                max_len_pos = len(str(arr[i]))
    if len(pos_arr) > 0:
        for i in range(10):
            sort_list_pos.append([])
        for i in range(0, max_len_pos):
            new_pos_arr = []
            for elem in pos_arr:
                category = (elem // 10 ** i) % 10
                sort_list_pos[category].append(elem)
            for mini_list in sort_list_pos:
                for elem1 in mini_list:
                    new_pos_arr.append(elem1)
            pos_arr = new_pos_arr
            sort_list_pos = []
            for j in range(10):
                sort_list_pos.append([])
    if len(neg_arr) > 0:
        for i in range(10):
            sort_list_neg.append([])
        for i in range(0, max_len_neg):
            new_neg_arr = []
            for elem in neg_arr:
                category = (elem // 10 ** i) % 10
                sort_list_neg[category].append(elem)
            for mini_list in sort_list_neg:
                for elem1 in mini_list:
                    new_neg_arr.append(elem1)
            neg_arr = new_neg_arr
            sort_list_neg = []
            for j in range(10):
                sort_list_neg.append([])
    
    arr = []
    for i in neg_arr[::-1]:
        arr.append(-i)
    for i in pos_arr:
        arr.append(i)

    return arr

def bucket_sort(arr: list[float]):
    """Функция bucket сортировки"""
    if len(arr) <= 1:
        return arr
    
    mn = min(arr)
    mx = max(arr)
    
    if mn == mx:
        return arr
    
    num_buckets = len(arr)
    range_val = mx - mn
    
    buckets = []
    for i in range(num_buckets):
        buckets.append([])
    
    for elem in arr:
        index = int((elem - mn) * (num_buckets - 1) / range_val)
        buckets[index].append(elem)
    
    for i in range(num_buckets):
        bucket = buckets[i]
        for j in range(len(bucket)):
            for k in range(len(bucket) - 1):
                if bucket[k] > bucket[k + 1]:
                    bucket[k], bucket[k + 1] = bucket[k + 1], bucket[k]
    
    result = []
    for bucket in buckets:
        for elem in bucket:
            result.append(elem)
    
    return result

def heap_sort(arr: list[int]):
    """Функция heap сортировки"""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        current = i
        while True:
            largest = current
            left = 2 * current + 1
            right = 2 * current + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != current:
                arr[current], arr[largest] = arr[largest], arr[current]
                current = largest
            else:
                break

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        current = 0

        while True:
            largest = current
            left = 2 * current + 1
            right = 2 * current + 2

            if left < i and arr[left] > arr[largest]:
                largest = left
            if right < i and arr[right] > arr[largest]:
                largest = right
                
            if largest != current:
                arr[current], arr[largest] = arr[largest], arr[current]
                current = largest
            else:
                break
    
    return arr
