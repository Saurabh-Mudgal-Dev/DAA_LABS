'''
Bubble sort and Insertion sort Performance Analysis
'''

def compare_bubble_insertion(random_data, sorted_data, reverse_data):
  result = ["Sorting Performance Report"]
  datasets = [("Random Dataset",random_data),
             ("Sorted Dataset",sorted_data),
             ("Reverse Dataset",reverse_data)]
  for name , array in datasets :
    b_arr, b_swap, b_comp = bubble_sort(array)
    i_arr, i_shift, i_comp = insertion_sort(array)
    b_str = " ".join(map(str,b_arr))
    i_str = " ".join(map(str,i_arr))

    if b_comp < i_comp:
      btr_algo = "Bubble Sort"
    elif b_comp > i_comp:
      btr_algo = "Insertion Sort"
    else: 
      btr_algo = "Both Equal"

    result.extend([
              name,
              f"Bubble Sorted: {b_str}",
              f"Bubble Comparisons: {b_comp}",
              f"Bubble Swaps: {b_swap}",
              f"Insertion Sorted: {i_str}",
              f"Insertion Comparisons: {i_comp}",
              f"Insertion Shifts: {i_shift}",
              f"Better Algorithm: {btr_algo}"
          ])
  return result
    
def bubble_sort (arr):
  comparison = 0
  swaps = 0 
  arr_copy = arr[:]
  n = len (arr_copy)

  for i in range (n):
    swapped = False
    for j in range (n-1-i):
      comparison += 1
      if arr_copy[j] > arr_copy[j+1]:
        arr_copy[j] , arr_copy[j+1] = arr_copy[j+1] , arr_copy[j]
        swaps += 1
        swapped = True 

    if not swapped:
      break
  return arr_copy , swaps , comparison

def insertion_sort (arr):
  comparison = 0
  shifts = 0 
  arr_copy = arr[:]
  n = len (arr_copy)

  for i in range (1,n):
    key = arr_copy[i]
    j = i -1 
    while j >= 0 : 
      comparison += 1
      if arr_copy [j] > key :
        arr_copy[j+1] = arr_copy[j]
        shifts += 1
        j -= 1
      else:
        break
    arr_copy[j+1] = key
  return arr_copy , shifts , comparison