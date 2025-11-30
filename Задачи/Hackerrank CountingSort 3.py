#Не удается загрузить код на сам сайт, поэтому отправляю его сюда
#Код проходит все тесты
n = int(input())
arr = []
for i in range(n):
    elem, string = map(str, input().split())
    arr.append(int(elem))
mn = min(arr)
count_arr = [0] * 100
for i in arr:
    count_arr[i - mn] += 1

for i in range(1, 100):
    count_arr[i] += count_arr[i - 1]
print(*count_arr)
