def linear_search(arr, x):                                              # Define a function to perform linear search
    for i in range(len(arr)):                                           # Iterate over each element of the array
        if arr[i] == x:                                                 # If the element is found, return its index
            return i
    return -1                                                           # If the element is not found, return -1


arr = [5, 2, 9, 1, 5, 6]                                                # Create an array and element to search
x = 5

result = linear_search(arr, x)                                          # Call the linear search function and store the result

if result == -1:                                                        # If the element is not found, print a message
    print("Element not found")
else:                                                                   # If the element is found, print its index
    print(f"Element found at index {result}")

'''
Element found at index 0
'''
