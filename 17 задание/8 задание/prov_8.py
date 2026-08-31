from itertools import *

k = 0

for i in product('01234567', repeat = 5):
	w = ''.join(i)
	if w.count('6') == 1:
		if all(d + '6' not in w and '6' + d not in w for d in '1357'):
			k += 1
print(k)
# 3381
