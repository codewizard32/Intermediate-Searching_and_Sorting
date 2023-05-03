def fibonacci_search(arr, x):                                           # Define a function to perform Fibonacci search
    fib2 = 0 # (m-2)th Fibonacci number                                 # Initialize Fibonacci numbers
    fib1 = 1 # (m-1)th Fibonacci number
    fib = fib2 + fib1 # mth Fibonacci number

    while fib < len(arr):                                               # Find smallest Fibonacci number greater than or equal to the length of the array
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1                                                         # Initialize offset

    while fib > 1:                                                      # Perform search
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and arr[offset+1] == x:                                     # If element is not found, return -1
        return offset + 1

    return -1                                                           # If element is not found, return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                       # Create an array and element to search
x = 5

result = fibonacci_search(arr, x)                                       # Call the Fibonacci search function and store the result

if result == -1:                                                        # If the element is not found, print a message
    print("Element not found")
else:                                                                   # If the element is found, print its index
    print(f"Element found at index {result}")

'''
Ouput:Element found at index 4
'''
