import math                                                             # Import the math module for square root function

def jump_search(arr, x):                                                # Define a function to perform jump search
    n = len(arr)
    step = int(math.sqrt(n))                                            # Determine the step size as the square root of n
    prev = 0
    while arr[min(step, n)-1] < x:                                      # Keep jumping until we find a block that contains x
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:                                                   # If we've jumped past the end of the array, x isn't there
            return -1
    while arr[prev] < x:                                                # Linear search within the block containing x
        prev += 1
        if prev == min(step, n):                                         # If we've reached the end of the block, x isn't there
            return -1
    if arr[prev] == x:                                                  # If we've found x, return its index
        return prev
    return -1                                                           # If we've exhausted the array without finding x, return -1


arr = [1, 2, 5, 5, 6, 9]                                                # Create an array and element to search
x = 5

result = jump_search(arr, x)                                            # Call the jump search function and store the result

if result == -1:                                                        # If the element is not found, print a message
    print("Element not found")
else:                                                                   # If the element is found, print its index
    print(f"Element found at index {result}")

'''OUTPUT
Element found at index 2
'''
