three = list(range(100, 1000))
three.reverse()
six = list(range(100000, 1000000))
six.reverse()

for i in six:
    i = str(i)
    if i[0]==i[5] and i[1]==i[4] and i[2]==i[3]:
        num = int(i)
        for n in three:
            g = num/n
            if g in three
        break
    else:
        continue

print(num)
