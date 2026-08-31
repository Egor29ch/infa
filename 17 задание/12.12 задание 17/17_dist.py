f = open('dist_1_17.txt')
a = []
sp_15 = []
min_pr = 100000000000000000
k = 0
for el in f:
    a.append(int(el))

for x in a:
    if x % 100 == 15 and len(str(abs(x))) == 3:
        sp_15.append(x)

for i in range(len(a) - 2):
    if (a[i] > 0 and a[i + 1] > 0 and a[i + 2] > 0) or (a[i] < 0 and a[i + 1] < 0 and a[i + 2] < 0):
        if (max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2])) > (min(sp_15) ** 2):
            k += 1
            min_pr = min(max(a[i], a[i + 1], a[i + 2]) * min(a[i], a[i + 1], a[i + 2]), min_pr)
print(k, min_pr)
# 3523 342684