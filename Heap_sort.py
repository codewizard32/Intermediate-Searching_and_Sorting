def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):                                                     # Build a max heap
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):                                                           # Extract elements from the heap one by one
        arr[i], arr[0] = arr[0], arr[i]                                                   # Swap the first element (max) with the last element
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i                                                                           # Initialize largest as root
    left = 2*i + 1                                                                        # Left child
    right = 2*i + 2                                                                       # Right child

    if left < n and arr[left] > arr[largest]:                                             # Check if left child is larger than root
        largest = left

    if right < n and arr[right] > arr[largest]:                                           # Check if right child is larger than largest so far
        largest = right

    if largest != i:                                                                      # If the largest element is not the root, swap them
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)                                                          # Recursively heapify the affected sub-tree


arr = input("Enter a list of numbers separated by spaces: ")
arr = [int(num) for num in arr.split()]

sorted_arr = heap_sort(arr)

print("Sorted array:", sorted_arr)

'''
Enter a list of numbers separated by spaces: 5 3 8 4 2 7 1 6
Sorted array: [1, 2, 3, 4, 5, 6, 7, 8]
'''
