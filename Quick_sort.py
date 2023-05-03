def quick_sort(arr):
    if len(arr) <= 1:                         # Base case: if the array has 0 or 1 element, it's already sorted
        return arr

    pivot = arr[0]                            # Choose the first element as the pivot
    left = []                                 # Initialize an empty list for elements less than the pivot
    right = []                                # Initialize an empty list for elements greater than the pivot
    for i in range(1, len(arr)):
        if arr[i] < pivot:                    # If the element is less than the pivot, add it to the left list
            left.append(arr[i])
        else:                                 # If the element is greater than or equal to the pivot, add it to the right list
            right.append(arr[i])
    
    left = quick_sort(left)                   # Recursively sort the left list
    right = quick_sort(right)                 # Recursively sort the right list

    return left + [pivot] + right              # Concatenate the sorted left list, the pivot, and the sorted right list


arr = input("Enter a list of numbers separated by spaces: ")            # Take input from the user
arr = [int(num) for num in arr.split()]

sorted_arr = quick_sort(arr)                                           # Sort the array using quick sort

print("Sorted array:", sorted_arr)                                      # Print the sorted array

'''OUTPUT:
Enter a list of numbers separated by spaces:5 2 9 1 5 6
Sorted array: [1, 2, 5, 5, 6, 9]
'''



