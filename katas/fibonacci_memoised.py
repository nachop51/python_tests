fibcache = {}
def fibonacci(num):
    if num in fibcache:
        return fibcache[num]
    else:
        fibcache[num] = num if num < 2 else fibonacci(num-1) + fibonacci(num-2)
        return fibcache[num]