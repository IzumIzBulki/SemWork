def max1(a, b):
    if a > b:
        return a
    return b
def fibonachi(n):
    if n in [1, 2]:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)
def quic_sort(array):   # быстрая сортировка
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less1 = [i for i in array[1:] if i <= pivot]
    less2 = [i for i in array[1:] if i > pivot]
    return quic_sort(less1) + [pivot] + quic_sort(less2)
def merge_sort(numm):    # сортировка слиянием
    if len(numm) > 1:
        mid = len(numm) // 2
        left = numm[:mid]
        right = numm[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numm[k] = left[i]
                i += 1
            else:
                numm[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numm[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numm[k] = right[j]
            j += 1
            k += 1
