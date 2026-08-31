a = [1, 11, 21, 31, 41, 51 ,61, 71, 81, 91, 101]
k = 0
max_razn = -10000
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] % 2 != 0 and a[j] % 2 != 0) and (abs(a[i] - a[j]) % 10 == 0):
            k += 1
            max_razn = max(max_razn, abs(a[i] - a[j]))
print(k, max_razn)