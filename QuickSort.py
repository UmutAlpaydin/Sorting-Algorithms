def partition(arr, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    # Create a helper function that will be called recursively
    def _quick_sort(element, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(element, low, high)
            _quick_sort(element, low, split_index)
            _quick_sort(element, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)


# Let's run our algorithm with some random values
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)