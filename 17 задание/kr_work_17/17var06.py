f = open('17var06.txt')
a = []
k = 0
min_sum = 1000000000

for el in f:
    a.append(int(el))

for i in range(len(a) - 1):
    if a[i] % 30 == min(a) or a[i + 1] % 30 == min(a):
        k += 1
        min_sum = min(min_sum, a[i] + a[i + 1])
print(k, min_sum)
#679 5644