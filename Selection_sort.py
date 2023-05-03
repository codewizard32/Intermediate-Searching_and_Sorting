def selection_sort(arr):
    n = len(arr)                                                        # Get the length of the array
    for i in range(n):                                                  # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]                     # Swap the found minimum element with the first element

    return arr                                                          # Return the sorted array


arr = input("Enter a list of numbers separated by spaces: ")            # Take input from the user
arr = [int(num) for num in arr.split()]

sorted_arr = selection_sort(arr)                                        # Sort the array using selection sort

print("Sorted array:", sorted_arr)                                      # Print the sorted array

'''OUTPUT
Enter a list of numbers separated by spaces: 3 1 4 1 5 9 2 6 5 3
Sorted array: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
'''
