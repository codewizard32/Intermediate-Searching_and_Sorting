def merge_sort(arr):
    if len(arr) == 1:                                                      # Base case: if the array has only one element, return it
        return arr
    
    mid = len(arr) // 2                                                    # Split the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]
   
    sorted_left = merge_sort(left_half)                                    # Recursively sort the left and right halves
    sorted_right = merge_sort(right_half)
    
    merged_arr = []                                                        # Merge the two sorted halves
    left_index = 0
    right_index = 0
    
    while left_index < len(sorted_left) and right_index < len(sorted_right):
        if sorted_left[left_index] < sorted_right[right_index]:
            merged_arr.append(sorted_left[left_index])
            left_index += 1
        else:
            merged_arr.append(sorted_right[right_index])
            right_index += 1
    
    merged_arr += sorted_left[left_index:]                                 # Add any remaining elements from the left or right array
    merged_arr += sorted_right[right_index:]
    
    return merged_arr


arr = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in arr.split()]

sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)

'''OUTPUT
Enter a list of numbers separated by spaces: 3 6 1 8 2 9
Sorted array: [1, 2, 3, 6, 8, 9]
'''
