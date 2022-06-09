def f(x, a):
    return ((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0)))

for a in range(1, 1001):
    for x in range(1, 1001):
        if not f(x, a):
            break
    else:
        print(a)
        continue
    