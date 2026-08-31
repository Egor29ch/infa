from itertools import *

k = 0
count = 0

for i in product(sorted('ФЛАМИНГО'), repeat = 5):
	w = ''.join(i)
	k += 1
	if k % 2 != 0:
		if w[0] != 'Н' and w.count('О') <= 1:
			count += 1
print(count)
# 11907