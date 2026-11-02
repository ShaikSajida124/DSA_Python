def binary_search(arr, item, start, end):
  if start <= end:
    mid = (start+end)//2
    if arr[mid] == item:
      return mid
    elif item < arr[mid]:
      return binary_search(arr, item, start, mid-1)
    else:
      return binary_search(arr, item, mid+1, end)


