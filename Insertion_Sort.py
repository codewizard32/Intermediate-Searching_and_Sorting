def insertion_sort(arr):
    n = len(arr)                                                        # Get the length of the array
    for i in range(1, n):                                               # Traverse through the array starting from index 1
        key = arr[i]                                                    # Store the current element as the key
        j = i-1                                                         
        while j >= 0 and key < arr[j]:                                  # Compare the key with each element before it
            arr[j+1] = arr[j]                                           # If the element is greater than the key, move the element to the right
            j -= 1                                                      # Continue comparing with the previous elements
        arr[j+1] = key                                                  # Insert the key in the correct position
    return arr                                                          


arr = input("Enter a list of numbers separated by spaces: ")            # Take input from the user
arr = [int(num) for num in arr.split()]

sorted_arr = insertion_sort(arr)                                        # Sort the array using insertion sort

print("Sorted array:", sorted_arr)                                      # Print the sorted array

'''OUTPUT
Enter a list of numbers separated by spaces: 5 3 8 4 2 7 1 6
Sorted array: [1, 2, 3, 4, 5, 6, 7, 8]
'''
