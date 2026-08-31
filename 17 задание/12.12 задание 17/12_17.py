f = open('12_17.txt')
a = []
k = 0
sum_el = 0
min_2 = []
for el in f:
    a.append(int(el))
for x in a:
    if len(str(x)) == 2:
        min_2.append(x)
for i in range(len(a) - 1):
    if (len(str(a[i])) == 2 and len(str(a[i + 1])) != 2) or (len(str(a[i])) != 2 and len(str(a[i + 1])) == 2) and ((a[i] + a[i + 1]) % min(min_2) == 0):
        k += 1
        sum_el = max(sum_el, a[i] + a[i + 1])
print(k, sum_el)
#908 10026