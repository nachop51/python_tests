def digitize(n):
    l = []
    s = str(n)
    for i in s[::-1]:
        l.append(int(i))
    return l

print(digitize(35231))

# best solution:
# def digitize(n):
    # return map(int, str(n)[::-1])