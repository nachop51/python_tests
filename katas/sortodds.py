def sort_array(source_array):
    # Return a sorted array.
    if source_array == []:
        return source_array
    odds = []
    for i in source_array:
        if i % 2 != 0:
            odds.append(i)
    odds.sort(reverse=True)
    j = 0
    for i in source_array:
        if i % 2 != 0:
            source_array[j] = odds.pop()
        j += 1
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))