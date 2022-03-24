def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)


t = [x for x in powers_of_2(5)]
print(t)

t = list(powers_of_2(3))
print(t)

for i in range(20):
    if i in powers_of_2(4):
        print(i)

