
the_list = [1 if x % 2 == 0 else 0 for x in range(10)] # create a list
the_generator = (1 if x % 2 == 0 else 0 for x in range(10)) # create a generator

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

'''
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()
'''
