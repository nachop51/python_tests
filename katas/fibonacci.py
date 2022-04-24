def nth_fib(n):
    if n == 1:
        return 0
    n1 = 0
    n2 = 1
    i = 1
    while i < n:
        new = n1 + n2
        n2 = n1
        n1 = new
        i += 1
    return new

print(nth_fib(1))
print(nth_fib(2))
print(nth_fib(3))
print(nth_fib(4))
print(nth_fib(5))
print(nth_fib(6))
print(nth_fib(7))
print(nth_fib(8))
print(nth_fib(9))