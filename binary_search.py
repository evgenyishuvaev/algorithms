def bin_search(lst, item):
    low = 0
    high = len(lst) - 1
    c = 1
    while low <= high:
        print(c)
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        c += 1
    return


l = [i for i in range(1, 1001)]
print(bin_search(l, 875))