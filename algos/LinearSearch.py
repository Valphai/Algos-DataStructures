def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return array[i]
    return None