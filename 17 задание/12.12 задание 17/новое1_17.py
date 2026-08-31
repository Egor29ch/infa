f = open('новое1_17.txt')
a = []
sp_33 = []
count = 0
max_sum = 0
for el in f:
    a.append(int(el))

# for x in range(len(a) - 2):
#     if (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) != 2) or (len(str(abs(a[x]))) != 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) == 2) or (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) != 2 and len(str(abs(a[x + 2]))) == 2):
#         list_2.append(a[x])
#         list_2.append(a[x + 1])
#         list_2.append(a[x + 2])
for c in a:
    if abs(c) % 100 == 33:
        sp_33.append(c)

for x in range(len(a) - 2):
    if (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) != 2) or (len(str(abs(a[x]))) != 2 and len(str(abs(a[x + 1]))) == 2 and len(str(abs(a[x + 2]))) == 2) or (len(str(abs(a[x]))) == 2 and len(str(abs(a[x + 1]))) != 2 and len(str(abs(a[x + 2]))) == 2):
        if (a[x] + a[x + 1] + a[x + 2]) ** 2 < max(sp_33):
            count += 1
            max_sum = max(max_sum, a[x] + a[x + 1] + a[x + 2])
print(count, max_sum)
# 68 306