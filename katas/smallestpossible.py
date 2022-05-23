def solution(a):
    if len(a) <= 1:
        return sum(a)
    while len(set(a)) != 1:
        a = sorted(a)
        a[-1] = a[-1] - a[-2]
    return sum(a)


print(solution([6, 9, 21]))
