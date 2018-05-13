import numpy as np
import sys

arr=np.array([[100, 200, 150, 90, 300, 400], [200, 120, 230, 80, 100, 9000]])

print(arr)
print(arr.ndim)
print(arr.shape)

arr=arr.reshape(12)
print(np.median(np.sort(arr)))  # 排序查中位数



# arr2 = np.array([1, 2, 3, 4, 5, 6])
# arr2.shape(3, 2)
# print(123)
# print(arr2)