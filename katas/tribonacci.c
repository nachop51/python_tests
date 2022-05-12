#include <stdlib.h>
#include <stdio.h>

long long *tribonacci(const long long signature[3], size_t n);
void print_array(long long *array, size_t n);

int main(void)
{
	const long long signature[3] = {1, 1, 1};
	const long long signature2[3] = {0, 0, 1};
	const long long signature3[3] = {0, 1, 1};
	const long long signature4[3] = {0, 0, 0};
	long long *array;
	long long *array2;
	long long *array3;
	long long *array4;

	array = tribonacci(signature, 10);
	array2 = tribonacci(signature2, 1);
	// array3 = tribonacci(signature3, 3);
	array4 = tribonacci(signature4, 0);
	print_array(array, 10);
	print_array(array2, 1);
	print_array(array4, 0);
	free(array);
	free(array2);
	free(array4);

	return (0);
}

void print_array(long long *array, size_t n)
{
	size_t i;

	if (!array)
	{
		printf("(null)\n");
		return;
	}
	for (i = 0; i < n; i++)
	{
		printf("%lld", array[i]);
		if (i != n - 1)
		{
			putchar(44);
			putchar(32);
		}
	}
	putchar(10);
}

long long *tribonacci(const long long signature[3], size_t n) {

	//  <----  inizio!
	long long f = signature[0];
	long long s = signature[1];
	long long t = signature[2];
	long long result = 0;
	long long *array;
	size_t i;

	if (n == 0)
		return NULL;
	array = malloc(sizeof(long long) * n);
	if (n == 1)
	{
		array[0] = signature[0];
		return (array);
	}
	if (n == 2)
	{
		array[0] = f;
		array[1] = s;
		return (array);
	}
	if (n == 3)
		return (long long *)signature;
	array[0] = f;
	array[1] = s;
	array[2] = t;
	for (i = 3; i < n; i++)
	{
		result = f + s + t;
		f = s;
		s = t;
		t = result;
		array[i] = result;
	}
	return array;
}