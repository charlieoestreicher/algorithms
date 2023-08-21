def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

print(linear_search(lst, target))
