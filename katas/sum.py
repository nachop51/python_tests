def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    sum = 0
    if a < b:
        for i in range(a, b+1):
            sum += i
    else:
        for i in range(b, a + 1):
            sum += i
    return sum

print(get_sum(0, 1))
print(get_sum(-1, 2))
print(get_sum(0, -1))