def algorithm(n, m):
	remainder = 0
	while n > 1:
		if n % 2 == 0:
			m *= 2
			n /= 2
		else:
			remainder += m
			m *= 2
			n = (n - 1) / 2 

	return m + remainder
