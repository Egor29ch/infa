f = open('17kr5.txt')
a = []
k = 0
max_sum = 0
sp_6 = []

for el in f:
    a.append(int(el))

for x in a:
    if abs(x) % 10 == 6:
        sp_6.append(x)

for i in range(len(a) - 1):
    if (abs(a[i]) % 10 == 6 and abs(a[i + 1]) % 10 != 6) or (abs(a[i]) % 10 != 6 and abs(a[i + 1]) % 10 == 6) and ((a[i] ** 2 + a[i + 1] ** 2) < min(sp_6) ** 2):
            k += 1
            max_sum = max(max_sum, a[i] ** 2 + a[i + 1] ** 2)

print(k, max_sum)

# 825 193513601