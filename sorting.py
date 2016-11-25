from timing import timing


@timing
def bubble_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array), 0, -1):
        for j in range(i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


@timing
def insertion_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


@timing
def selection_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        smallest = array[i]
        smallest_index = i
        for j in range(i, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
    return array


def quick_sort(array):
    if len(array) == 0 or array is None:
        return []
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    pivot = array[0]
    left_sublist_end_index = 0
    right_sublist_start_index = len(array)-1
    while left_sublist_end_index < right_sublist_start_index:
        if array[left_sublist_end_index + 1] > pivot:
            array[left_sublist_end_index + 1], array[right_sublist_start_index] = \
                array[right_sublist_start_index], array[left_sublist_end_index + 1]
            right_sublist_start_index -= 1
        else:
            left_sublist_end_index += 1

    left = quick_sort(array[1:left_sublist_end_index+1])
    right = (quick_sort(array[right_sublist_start_index+1:len(array)]))

    return left + [pivot] + right


def merge_sort(array):

    if len(array) <= 1:
        return array

    a = merge_sort(array[0:int(len(array)/2)])
    b = merge_sort(array[(int(len(array)/2)):len(array)])

    return_array = []

    j = 0
    k = 0
    for i in range(len(a) + len(b)):
        if j >= len(a):
            return_array.append(b[k])
            k += 1
        elif k >= len(b):
            return_array.append(a[j])
            j += 1
        elif a[j] <= b[k]:
            return_array.append(a[j])
            j += 1
        else:
            return_array.append(b[k])
            k += 1

    return return_array


@timing
def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array)):
        array[len(array)-1-i], array[0] = array[0], array[len(array)-1-i]
        heapify(array, 0, len(array)-i-1)
    return array


def build_max_heap(array):
    for i in range(int(len(array)/2-1), -1, -1):
        heapify(array, i, len(array))


def heapify(array, i, n):

    left = 2*i + 1
    right = 2*i + 2

    largest_index = i

    if left < n and array[left] > array[largest_index]:
        largest_index = left
    if right < n and array[right] > array[largest_index]:
        largest_index = right

    if largest_index != i:
        array[i], array[largest_index] = array[largest_index], array[i]
        heapify(array, largest_index, n)


