def heapify(arr, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    n = len(arr)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Let's run our algorithm with some random values
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)