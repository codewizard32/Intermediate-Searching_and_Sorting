def ternary_search(arr, l, r, x):                                        # Define a function to perform ternary search
    if r >= l:                                                          # Check if right index is greater than or equal to left index
        mid1 = l + (r - l) // 3                                          # Calculate first middle index
        mid2 = r - (r - l) // 3                                          # Calculate second middle index
        if arr[mid1] == x:                                               # If the element is found at first middle index, return the index
            return mid1
        elif arr[mid2] == x:                                             # If the element is found at second middle index, return the index
            return mid2
        elif x < arr[mid1]:                                              # If the element is smaller than the element at first middle index, search in the left part of array
            return ternary_search(arr, l, mid1 - 1, x)
        elif x > arr[mid2]:                                              # If the element is greater than the element at second middle index, search in the right part of array
            return ternary_search(arr, mid2 + 1, r, x)
        else:                                                            # Otherwise, search in the middle part of array
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)
    return -1                                                            # If the element is not found, return -1

arr = [1, 2, 5, 5, 6, 9]                                                # Create an array and element to search
x = 5

result = ternary_search(arr, 0, len(arr) - 1, x)                         # Call the ternary search function and store the result

if result == -1:                                                        # If the element is not found, print a message
    print("Element not found")
else:                                                                   # If the element is found, print its index
    print(f"Element found at index {result}")

'''OUTPUT
Element found at index 2
'''
