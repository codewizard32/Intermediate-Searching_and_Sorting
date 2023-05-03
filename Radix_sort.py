def counting_sort(arr, exp1):
    n = len(arr)
    output = [0] * (n)                                                           # The output array that will have sorted arr
    count = [0] * (10)                                                           # Initialize count array as 0

    for i in range(0, n):                                                        # Store count of occurrences in count[]
        index = arr[i] // exp1
        count[index % 10] += 1

                                                                                 # Change count[i] so that count[i] now contains actual                   
    for i in range(1, 10):
        count[i] += count[i - 1]                                                 # position of this digit in output[]  

    i = n - 1                                                                    # Build the output array
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
                                                                                      
    i = 0                                                                        # Copying the output array to arr[],
    for i in range(0, len(arr)):                                                 # so that arr now contains sorted numbers  
        arr[i] = output[i]

def radix_sort(arr):                                                             # Find the maximum number to know number of digits
    max1 = max(arr)
    exp = 1                                                                      # Do counting sort for every digit
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


arr = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in arr.split()]

sorted_arr = radix_sort(arr)

print("Sorted array:", sorted_arr)

'''
Enter a list of numbers separated by spaces: 170 45 75 90 802 24 2 66
Sorted array: [2, 24, 45, 66, 75, 90, 170, 802]
'''
