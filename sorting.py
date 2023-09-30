def get_smallest_subarray_to_sort(array: list[int]) -> tuple[int, int]:
    first_index = -1
    last_index = -1

    for i in range(1, len(array)):
        key = array[i]

        if key >= array[i - 1]:
            continue

        last_index = i

        j = i -1
        while j >= 0 and key < array[j]:
            if first_index == -1 or first_index > j:
                first_index = j

            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return (first_index, last_index)
