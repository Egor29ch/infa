f = open('17var17.txt')
a = []
max_sum = -100000000000000000000000000000000000000000000000000000000000000
k = 0
def true_kvadrat(n):
	if n >= 0:
		if round(n) ** 0.5 * round(n ** 0.5) == abs(n):
			return 1
		else:
			return 0

for el in f:
	a.append(int(el))

for i in range(len(a) - 1):
	if true_kvadrat(a[i]) == 1 or true_kvadrat(a[i + 1]) == 1:
		k += 1
		max_sum = max(max_sum, a[i] + a[i + 1])

print(k, max_sum)
#60 18555