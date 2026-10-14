def modified_bubble_sort(arr):
  for i in range(len(arr)-1):
    is_swap = False
    for j in range(len(arr)-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        is_swap = True
    if not is_swap:
      break
