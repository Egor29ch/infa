f_A = open('27-A_demo (1).txt')
f_B = open('27-B_demo (2).txt')
sp_a = [ ]
sp_b = [] 
sp_1_a = []
sp_2_a = []

#Вычленяю каждое число из файла
for a in f_A:
    print(a.split('  '))
    print(len(a))
    n_1 = a[0]
    n_2 = a[1]
    sp_1_a.append(n_1)
    sp_2_a.append(n_2)
    break
for x in sp_1_a:
    for y in sp_2_a:
        if x % 3 != 0 and y % 3 == 0


