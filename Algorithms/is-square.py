import math
import timeit

def IsSquare(n):
    sqrt_n = int(math.sqrt(n))
    return n == sqrt_n ** 2

def IsSquare2(n):
    h = n & 0xF
    if h > 9:
        return False
    if h in (2, 3, 5, 6, 7, 8):
        return False
    sqrt_n = int(math.sqrt(n))
    return n == sqrt_n ** 2

def IsSquare3(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0

for i in range(100):
    R1 = IsSquare(i)
    R2 = IsSquare2(i)
    R3 = IsSquare3(i)
    if R1 != R2 or R1 != R3:
        print(i, R1, R2, R3)

print(timeit.timeit('for i in range(100000): IsSquare(i)', setup = 'from __main__ import IsSquare', number = 1))
print(timeit.timeit('for i in range(100000): IsSquare2(i)', setup = 'from __main__ import IsSquare2', number = 1))
print(timeit.timeit('for i in range(100000): IsSquare3(i)', setup = 'from __main__ import IsSquare3', number = 1))

