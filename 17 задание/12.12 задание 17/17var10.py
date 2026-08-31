f = open('17var10.txt')
a = []
k = 0
max_sum = 0
sp_100 = []

def dvuznach(n):
    if len(str(n)) == 3:
        return 1
    else:
        return 0

for x in f:
    a.append(int(x))

for el in a:
    if el % 1000 == 100:
        sp_100.append(el)

for i in range(len(a) - 2):
    if dvuznach(a[i]) + dvuznach(a[i + 1]) + dvuznach(a[i + 2]) == 2:
        if a[i] + a[i + 1] + a[i + 2] <= max(sp_100):
            max_sum = max(a[i] + a[i + 1] + a[i + 2], max_sum)
            k += 1
print(k, max_sum)
