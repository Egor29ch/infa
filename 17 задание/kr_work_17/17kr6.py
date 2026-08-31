f = open('17kr6.txt')
a = []
sp_123 = []
k = 0
max_sum = 0

def num_5(x):
    return 9999 < abs(x) < 100000

for el in f:
    a.append(int(el))

for y in a:
    if y % 1000 == 123:
        sp_123.append(y)

for i in range(len(a) - 2):
    if (num_5(a[i]) + num_5(a[i + 1]) + num_5(a[i + 2])) == 2:
        if (a[i] % 3 == 0 and a[i + 1] % 3 != 0 and  a[i + 2] % 3 != 0) or (a[i] % 3 != 0 and a[i + 1] % 3 != 0 and  a[i + 2] % 3 == 0) or (a[i] % 3 != 0 and a[i + 1] % 3 == 0 and  a[i + 2] % 3 != 0):
            if (a[i] + a[i + 1] + a[i + 2]) > max(sp_123):
                k += 1
                max_sum = max(max_sum, a[i] + a[i + 1] + a[i + 2])
print(k, max_sum)
# 63033