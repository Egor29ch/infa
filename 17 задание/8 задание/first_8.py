from itertools import *
k = 0
for i in product('012345', repeat=6):
    w = ''.join(i)
    if w[0] != 0:
        if w.count('0') == 1: 
            count = 0
            for x in '135':
                if x + '0' in w or '0' + x in w:
                    count += 1
            if count == 0:
                k += 1
print(k)
