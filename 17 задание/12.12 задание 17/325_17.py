f = open('325_17.txt')
a = []
k = 0
max_sum = 0
for el in f:
    a.append(int(el))

for i in range(len(a) - 1):
    if  ((a[i] % 21) + (a[i + 1] % 21)) == min(a):
        k += 1
        max_sum = max(max_sum, a[i] + a[i + 1])
print(k, max_sum)
# 213 171263