def selection_sort(array):
    for i in range(len(array)):
        smol = min(array[i:])
        if array[i] > smol:
            ind = array.index(smol,i)
            cache = array[i]
            array[i] = smol
            array[ind] = cache
    return array
