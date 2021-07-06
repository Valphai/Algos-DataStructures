from Testing import verify

@verify
def binary_search(array, target):
    array.sort()
    lower_b, upper_b = 0, len(array) - 1
    while lower_b <= upper_b:
        mid = (lower_b + upper_b)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            upper_b = mid + 1
        else:
            lower_b = mid - 1
    return None

@verify
def rec_binary_search(array, target):
    array.sort()
    mid = len(array)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        rec_binary_search(array[mid + 1:], target)
    else:
        rec_binary_search(array[:mid - 1], target)
    return None