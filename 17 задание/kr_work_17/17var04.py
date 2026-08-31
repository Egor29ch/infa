f = open('17var04.txt')
a = []
k = 0
max_sum = - 10000000000
sp_250 = []

for el in f:
    a.append(int(el))

for x in a:
    if abs(x) % 1000 == 250:
        sp_250.append(x)

for i in range(len(a) - 2):
    if abs(a[i]) % 2 == 0 and abs(a[i + 1]) % 2 == 0 and abs(a[i + 2]) % 2 == 0:
        if (a[i] + a[i + 1] + a[i + 2]) > min(sp_250):
            k += 1
            max_sum = max(max_sum, a[i] + a[i + 1] + a[i + 2])

print(k, max_sum)
#5706 275182