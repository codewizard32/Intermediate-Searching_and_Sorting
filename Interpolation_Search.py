def interpolation_search(arr, x):
    lo = 0                                                                  # Set the lower bound of the search range to 0
    hi = len(arr) - 1                                                       # Set the upper bound of the search range to the last index of the array
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:                        # Perform the search while the search range is valid and the search element is within the range
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo])) * (x - arr[lo])       # Calculate the position of the search element using interpolation formula
        if arr[pos] == x:                                                   
            return pos                                                       # If the search element is found, return its index
        elif arr[pos] < x:
            lo = pos + 1                                                     
        else:
            hi = pos - 1                                                     
    return -1                                                                 # If the search element is not found, return -1


arr = [1, 2, 5, 5, 6, 9]                                                     # Create an array and element to search
x = 5

result = interpolation_search(arr, x)                                        # Call the interpolation search function and store the result

if result == -1:                                                             
    print("Element not found")                                               # If the element is not found, print a message
else:                                                                        
    print(f"Element found at index {result}")                                # If the element is found, print its index

'''OUTPUT:
Element found at index 2
'''
