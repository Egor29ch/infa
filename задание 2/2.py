print('x z w y')

for x in 0,1:
    for z in 0,1:
        for w in 0,1:
            for y in 0,1:
                cv = not(z)
                if (not((x == cv) and (y <= w)) <= x) == 1:
                    print(x, z, w, y)