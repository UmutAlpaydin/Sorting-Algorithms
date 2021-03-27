def insertion_sort(arr):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(arr)):
        element = arr[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and arr[j] > element:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the item
        arr[j + 1] = element


#Let's run our algorithm with some random values
unsorted_arr = [9, 1, 15, 28, 6]
insertion_sort(unsorted_arr)
print(unsorted_arr)