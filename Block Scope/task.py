def is_prime(num):
    if num == 2:
        return True

    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

#trueorfalse = is_prime(67)

#print(trueorfalse)
num = 65
for i in range(55, num):
    print(i)