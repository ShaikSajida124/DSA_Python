def selection_sort(arr):
 for i in range(len(arr)-1):
  small_index = i
  for j in range(i+1, len(arr)):
    if arr[j] < arr[small_index]:
      small_index = j
  arr[i], arr[small_index] = arr[small_index], arr[i]
  
