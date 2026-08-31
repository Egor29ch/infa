f = open('313_17.txt')
a = []
k = 0
min_sum = 100001
for el in f:
    a.append(int(el))

for i in range(len(a) - 1):
    if  ((a[i] % 15) + (a[i + 1] % 15)) == min(a):
        k += 1
        min_sum = min(min_sum, a[i] + a[i + 1])
print(k, min_sum)
# 365 5888