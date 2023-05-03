def binary_search(arr, l, r, x):                              # Define a function to perform binary search
    while l <= r:                                             # Continue searching until the left index is less than or equal to the right index
        mid = l + (r - l) // 2                                # Calculate the middle index
        if arr[mid] == x:                                     # If the middle element matches the search element, return its index
            return mid
        elif arr[mid] < x:                                    # If the middle element is less than the search element, search the right half
            l = mid + 1
        else:                                                 # If the middle element is greater than the search element, search the left half
            r = mid - 1
    return -1                                                 # If the element is not found, return -1

arr = [1, 2, 5, 5, 6, 9]                                      # Create a sorted array to search
x = 5                                                         # Create an element to search for

result = binary_search(arr, 0, len(arr)-1, x)                 # Call the binary search function and store the result

if result == -1:                                              # If the element is not found, print a message
    print("Element not found")
else:                                                         # If the element is found, print its index
    print(f"Element found at index {result}")

''' 
OUTPUT: Element found at index 2
'''
