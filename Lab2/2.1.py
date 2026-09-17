'''
Merge Sort and Quick Sort Task Prioritization and Comparison Report
'''

def compare_merge_quick_tasks(tasks):
  merge_comp = 0
  quick_comp = 0

  def comes_before(a,b):
    if a[1] != b[1]:
      return a[1]>b[1]
    return a[0]<b[0]

  def merge_sort(arr):
    nonlocal merge_comp
    if len(arr) <= 1:
      return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
      merge_comp += 1
      if comes_before(left[i], right[j]):
        res.append(left[i])
        i += 1
      else:
        res.append(right[j])
        j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

  def partition(arr, low, high):
    nonlocal quick_comp
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
      quick_comp += 1
      if comes_before(arr[j], pivot):
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

  def quick_sort(arr, low, high):
    if low<high:
      pi = partition(arr, low, high)
      quick_sort(arr, low, pi-1)
      quick_sort(arr, pi+1, high)

  merge_res = merge_sort(tasks[:])
  quick_res = tasks[:]
  quick_sort(quick_res, 0, len(quick_res)-1)

  if merge_comp < quick_comp:
    better = "Merge Sort"
  elif quick_comp < merge_comp:
    better = "Quick Sort"
  else:
    better = "Both Equal"
        
  return ["Task Prioritization Report", "Merge Sort Result", *[f"{x[0]} {x[1]}" for x in merge_res], f"Merge Comparisons: {merge_comp}", "Quick Sort Result", *[f"{x[0]} {x[1]}" for x in quick_res], f"Quick Comparisons: {quick_comp}", f"Better Algorithm: {better}"]