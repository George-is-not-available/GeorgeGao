arr = [10, 1, 37, 19, 5, 21, 7, 12]
# 排序
arr.sort(reverse=True)
mid = len(arr) // 2
arr[mid:] = sorted(arr[mid:])
# 打印结果
print(arr)
