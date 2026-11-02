def binary_search(arr, item):
  left = 0
  right = len(arr)-1
  mid = (left+right)//2
  while left <= right:
    if arr[mid] == item:
      return mid
    elif item < arr[mid]:
      right = mid-1
    else:
      left = mid+1
    mid = (left+right)//2
  return -1
