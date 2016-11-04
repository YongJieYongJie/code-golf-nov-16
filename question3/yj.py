import math
def a(b):
    yield b
    if b == 1:
        yield 1
    else:
        while b != 1:
            if b%2 == 0:
                b = b ** 0.5
            else:
                b = b ** 1.5
            b = math.floor(b)
            yield b

for x in a(5):
    print(x) 
