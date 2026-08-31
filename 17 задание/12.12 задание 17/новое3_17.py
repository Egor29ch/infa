f = open('новое3_17.txt')
a = []
sp_17 = []
count = 0
max_sum = 0
for el in f:
    a.append(int(el))

for c in a:
    if abs(c) % 100 == 17:
        sp_17.append(c)

for x in range(len(a) - 2):
    if (len(str(abs(a[x]))) == 3 and len(str(abs(a[x + 1]))) != 3 and len(str(abs(a[x + 2]))) != 3) or (len(str(abs(a[x]))) != 3 and len(str(abs(a[x + 1]))) == 3 and len(str(abs(a[x + 2]))) != 3) or (len(str(abs(a[x]))) != 3 and len(str(abs(a[x + 1]))) != 3 and len(str(abs(a[x + 2]))) == 3):
        if a[x] + a[x + 1] + a[x + 2] < max(sp_17):
            count += 1
            max_sum = max(max_sum, a[x] + a[x + 1] + a[x + 2])
print(count, max_sum)
# 2781 85899