array =[]
r = 0

for num in range(2,600851475143):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       array.append (num)

for i in array:
    if (600851475143%i)==0:
        r = i
        continue
    else:
        continue
print (r)
