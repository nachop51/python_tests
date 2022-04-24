#   Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b keeping their order.
# 
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    #your code here
    if a is None or b is None:
        return a
    for item in b:
        while a.count(item) > 0:
            a.remove(item)
    return a

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))
print(array_diff([1,2,3], [1, 2]))

# very fun to solve
# best practice:
# def array_diff(a, b):
#    return [x for x in a if x not in b]