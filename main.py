from random import random
from timing import timing
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort


@timing
def run_quick_sort(array, answer):
    sorted_array = quick_sort(list(array))
    if sorted_array != answer:
        print(array)
        print(sorted_array)


@timing
def run_merge_sort(array, answer):
    sorted_array = merge_sort(list(array))
    if sorted_array != answer:
        print(array)
        print(sorted_array)


def run_sorting():
    array = [int(random() * 100) for x in range(100)]
    array[0] = 0
    answer = sorted(array)

    # sorted_array = bubble_sort(list(array))
    # if sorted_array != answer:
    #     print(array)
    #     print(sorted_array)
    #
    # sorted_array = insertion_sort(list(array))
    # if sorted_array != answer:
    #     print(array)
    #     print(sorted_array)
    #
    # sorted_array = selection_sort(list(array))
    # if sorted_array != answer:
    #     print(array)
    #     print(sorted_array)

    run_quick_sort(list(array), answer)

    run_merge_sort(list(array), answer)

    # sorted_array = heap_sort(list(array))
    # if sorted_array != answer:
    #     print(array)
    #     print(sorted_array)

run_sorting()