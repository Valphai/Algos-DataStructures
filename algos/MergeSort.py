def merge_sort(list): # O(n log n) = time compl
                      # O(n) = space compl
    def split(list): # O(log n)
        mid = len(list)//2
        return list[:mid], list[mid:]
        
    def merge(left, right): # O(n)
        output_list = []
        i, j = 0, 0
        
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                output_list.append(left[i])
                i += 1
            else:
                output_list.append(right[j])
                j += 1
        
        while len(left) > i:
            output_list.append(left[i])
            i += 1
        while len(right) > j:
            output_list.append(right[j])
            j += 1
        return output_list
        
    if len(list) <= 1:
        return list
    left_list, right_list = split(list)
    left, right = merge_sort(left_list), merge_sort(right_list)
    return merge(left, right)