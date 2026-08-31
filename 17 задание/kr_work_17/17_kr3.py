f = open('17kr3.txt')
a = []
k = 0
max_sum = 0
sp_7 = []

for el in f:
    a.append(int(el))

for x in a:
     if x % 10 == 7:
          sp_7.append(x)
          

for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 != 7 and abs(a[i + 1]) % 10 == 7) or (abs(a[i]) % 10 == 7 and abs(a[i + 1]) % 10 != 7))  and ((a[i] ** 2 + a[i + 1] ** 2) < min(sp_7) ** 2):
            k += 1
            max_sum = max(max_sum, a[i] ** 2 + a[i + 1] ** 2)

print(k, max_sum)
# 681 97856050