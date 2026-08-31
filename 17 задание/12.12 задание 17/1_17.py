f = open('1_17.txt')
a = []
k = 0
for h in f:
    a.append(int(h))
min_a = []
min_el = 99999999999999999999999999999
for x in a:
    if x % 100 == 15 and len(str(x)) == 3:
        min_a.append(x)
        
for i in range(len(a) - 2):
    if (a[i] > 0 and a[i + 1] > 0 and a[i + 2] > 0) or (a[i] < 0 and a[i + 1] < 0 and a[i + 2] < 0):
        min_s = min(a[i], a[i + 1], a[i + 2])
        max_s = max(a[i], a[i + 1], a[i + 2])
        if (min_s * max_s > min(min_a) ** 2):
            k += 1
            min_el = min(max_s * min_s, min_el)
print(k, min_el)
# 67    