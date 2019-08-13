x = 1
y = 1
while x<4000000:
    if (x%2)== 0:
        z = x+y
        x=z
        sum = x
    else:
        z = x+y
        x=z
    if (x%2)== 0:
        z = x+y
        y=z
        sum = y
    else:
        z = x+y
        y=z
print (sum)

