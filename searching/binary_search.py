# The data structure must be sorted.
# Access to any element of the data structure takes constant time.

def binary_search(lst, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return binary_search(lst, low, mid - 1, target)
        else:
            return binary_search(lst, mid + 1, high, target)
    else:
        return -1

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 7
# print(binary_search(lst, 0, len(lst)-1, target))
