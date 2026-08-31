f = open('17var05.txt')
a = []
max_sum = 0
k = 0

for el in f:
    a.append(int(el))

for i in range(len(a) - 1):
    if a[i] % 27 == min(a) or a[i + 1] % 27 == min(a):
        max_sum = max(max_sum, a[i] + a[i + 1])
        k += 1
print(k, max_sum)


