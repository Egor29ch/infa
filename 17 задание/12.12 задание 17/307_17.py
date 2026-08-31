f = open('307_17.txt')
a = []
k = 0
sum_el = 200000

for el in f:
    a.append(int(el))

for i in range(len(a) - 1):
    if a[i] % 55 == min(a):
        k += 1
        sum_el = min(sum_el, a[i] + a[i + 1])
print(k, sum_el)
#181 3716