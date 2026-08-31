a = [1, 9, 25, 33, 41, 49, 65, 73, 81, 97, 105]
k = 0
max_razn = 0
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (abs(a[i] - a[i + 1]) % 9 == 0):
        k += 1
        max_razn = max(abs(a[i] - a[i + 1]), max_razn)
print(max_razn, k)