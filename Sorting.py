def bubble_sort(arr: list[int]):
    for j in range(len(arr)):
        for elem in range(len(arr) - 1):
            if arr[elem] > arr[elem + 1]:
                arr[elem], arr[elem + 1] = arr[elem + 1], arr[elem]
    return arr

def quick_sort(arr: list[int]):
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
    mn = min(arr)
    count_arr = [0] * (max(arr) - min(arr) + 1)
    for i in arr:
        count_arr[i - mn] += 1
    arr = []
    for i in range(len(count_arr)):
        arr += [i + mn] * count_arr[i]
    return arr

print(bubble_sort([1, -3, 6, 4, -2, 9, 7, 8, 5]))
print(count_sort([1, -3, 6, 4, -2, 9, 7, 8, 5]))
print(quick_sort([1, -3, 6, 4, -2, 9, 7, 8, 5]))