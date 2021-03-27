def selection_sort(arr):
    # This value of i corresponds to how many values were sorted
    for i in range(len(arr)):
        # We assume that the first item of the unsorted segment is the smallest
        min_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]


# Let's run our algorithm with some random values
unsorted_arr = [12, 8, 3, 20, 11]
selection_sort(unsorted_arr)
print(unsorted_arr)