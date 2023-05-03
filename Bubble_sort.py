def bubble_sort(arr):
    n = len(arr)                                                        # Get the length of the array
    for i in range(n):                                                  # Traverse through all array elements
        for j in range(0, n-i-1):                                       # Traverse the array from 0 to n-i-1
            if arr[j] > arr[j+1]:                                       # check if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]                     # If true, swap the two elements
    return arr                                                          # Return the sorted array


arr = input("Enter a list of numbers separated by spaces: ")            # Take input from the user
arr = [int(num) for num in arr.split()]

sorted_arr = bubble_sort(arr)                                           # Sort the array using bubble sort

print("Sorted array:", sorted_arr)                                      # Print the sorted array

'''
OUTPUT: 
Enter a list of numbers separated by spaces: 8 4 1 5 9 2
Sorted array: [1, 2, 4, 5, 8, 9]
'''
