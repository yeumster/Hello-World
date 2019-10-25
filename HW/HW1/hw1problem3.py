def rng(length = 6):
    from random import randint
    code = ''
    for i in range(length):
        code += str(randint(0, 9))
    return code


print(rng())
for i in range(1, 10):
    print(rng(i))

print(rng())
print(rng())
print(rng())
