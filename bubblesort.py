def bubble_sort(arr):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Let's run our algorithm with some random values
unsorted_arr = [5, 2, 1, 8, 4]
bubble_sort(unsorted_arr)
print(unsorted_arr)