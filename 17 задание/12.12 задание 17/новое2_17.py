f = open('новое2_17.txt')
a = []
sp_13 = []
count = 0
max_sum = 0
for el in f:
    a.append(int(el))

for c in a:
    if abs(c) % 100 == 13:
        sp_13.append(c)

for x in range(len(a) - 2):
    if (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) != 2) or (len(str(abs(a[x]))) != 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) == 2) or (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) != 2 and len(str(abs(a[x + 2]))) == 2):
        if a[x] + a[x + 1] + a[x + 2] <= max(sp_13):
            count += 1
            max_sum = max(max_sum, a[x] + a[x + 1] + a[x + 2])
print(count, max_sum)
# 1028 98584