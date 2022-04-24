def tribonacci(signature, n):
    list = []
    if n == 0:
        return list
    f, s, t = signature[0], signature[1], signature[2]
    if n == 1:
        return [f]
    elif n == 2:
        return [f, s]
    list.append(f), list.append(s), list.append(t)
    for i in range(n - 3):
        f, s, t = s, t, f+s+t
        list.append(t)
    return list

print(tribonacci([1, 1, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([1, 1, 1], 2))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 0, 0], 10))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([1, 2, 3], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 10))
print(tribonacci([300, 200, 100], 0))
print(tribonacci([0.5, 0.5, 0.5], 30))


# C solve!

# long long *tribonacci(const long long signature[3], size_t n) {
# 
	# //  <----  inizio!
	# long long f = signature[0];
	# long long s = signature[1];
	# long long t = signature[2];
	# long long result = 0;
	# long long *array;
	# size_t i;
# 
	# if (n == 0)
		# return NULL;
	# array = malloc(sizeof(long long) * n);
	# if (n == 1)
	# {
		# array[0] = signature[0];
		# return (array);
	# }
	# if (n == 2)
	# {
		# array[0] = f;
		# array[1] = s;
		# return (array);
	# }
	# if (n == 3)
		# return (long long *)signature;
	# array[0] = f;
	# array[1] = s;
	# array[2] = t;
	# for (i = 3; i < n; i++)
	# {
		# result = f + s + t;
		# f = s;
		# s = t;
		# t = result;
		# array[i] = result;
	# }
	# return array;
# }