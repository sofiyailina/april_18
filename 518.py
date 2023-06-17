def algo(n):
    for _ in range(3):
        n_s= str(n)
        odd_count = sum([int(d) % 2 != 0 for d in n_s])
        even_count = len(n_s) - odd_count
        if even_count > odd_count:
            n = n * 2 +1
        elif odd_count > even_count:
            n = n * 2 + n % 2
    return n
count = 0
for n in range(15_000, 150_000_000):
    res = algo(n)
    if 123455 <= res <= 987654321:
        count += 1
    if n % 1000000 == 0:
        print('*', end='')
print()
print(count)
