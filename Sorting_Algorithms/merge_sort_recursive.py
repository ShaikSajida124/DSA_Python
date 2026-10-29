def merge_sort(arr, start, end):
  if start < end:
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
  i = start
  j = mid+1
  temp = []

  #sort
  while i <= mid and j <= end:
    if arr[i] <= arr[j]:
      temp.append(arr[i])
      i += 1
    else:
      temp.append(arr[j])
      j += 1
  while i <= mid:
    temp.append(arr[i])
    i += 1
  while j <= end:
    temp.append(arr[j])
    j += 1

  #merge
  for i in range(len(temp)):
    arr[start+i] = temp[i]
