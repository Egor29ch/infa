f = open('17_kr2.txt')
a = []
sum_arif = 0
k_arif = 0
k = 0
max_sum = 0

for el in f:
    a.append(int(el))

for x in a:
    if x % 2 != 0:
        sum_arif += x
        k_arif += 1

sr_arif = sum_arif / k_arif

for i in range(len(a) - 1):
    if (a[i] % 5 == 0 and a[i + 1] < sr_arif) or (a[i] < sr_arif and a[i + 1] % 5 == 0):
            k += 1
            max_sum = max(max_sum, a[i] + a[i + 1])

print(k, max_sum)
# 1061 14847
