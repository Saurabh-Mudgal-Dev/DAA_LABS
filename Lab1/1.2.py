'''
Linear search and Binary search Comparison
'''

def compare_search_algorithms(arr, target):
  linear_index = binary_index = -1
  linear_count = binary_count = 0 

  for i in range(len(arr)):
    linear_count += 1
    if arr[i] == target:
      linear_index = i
      break 

  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left+right)//2
    binary_count += 1

    if arr[mid] == target :
      binary_index = mid
      right = mid - 1
    elif arr[mid] < target :
      left = mid + 1
    else: 
      right = mid - 1

    if binary_count > linear_count :
      btr_algo = "Linear Search" 
    elif binary_count < linear_count :
      btr_algo = "Binary Search"
    else:
      btr_algo = "Both Equal"
      
  return ["Search Comparison Report",
          "Linear Search",
          f"Index: {linear_index}",
          f"Comparisons: {linear_count}",
          "Binary Search",
          f"Index: {binary_index}",
          f"Comparisons: {binary_count}",
          f"Better Algorithm: {btr_algo}"]