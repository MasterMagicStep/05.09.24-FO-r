numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#простые
p = []
#составные
NeProsto = []
#
for i in numbers:
    if i == 1:
        continue
    is_p = True
    for j in range(2,i):
        if i % j == 0:
            is_p = False
            break
    if is_p :
        p.append(i)
    else:
        NeProsto.append(i)
    #
print(p)
print(NeProsto)