def quick_sort(array):
    if len(array) == 0:
        return []
    if len(set(array)) == 1:
        return array
    pivot = array[0]
    less = []
    equal = []
    more = []
    for i in array:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            more.append(i)
    return (quick_sort(less) + quick_sort(equal) + quick_sort(more))
