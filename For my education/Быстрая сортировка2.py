def quick_sort(a):
    if len(a) > 1:
        x = a[0]
        left = [element for element in a if element < x]
        mid = [element for element in a if element == x]
        right = [element for element in a if element > x]
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return a


c = [8, 9, 0, 1, 2, 6, 3]
print(quick_sort(c))
