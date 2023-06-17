def f(x, A):
    return((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 == 0) <= (x & A !=0))
for A in range(0, 100):
    if all(f(x, A) for x in range(0, 10000)):
        print(A)
        break