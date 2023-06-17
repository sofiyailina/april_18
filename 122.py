def redaktor(s):
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    return s

def  check_sum_digits(s):
    sum_d = sum([int(d) for d in s])
    d = 2
    while d**2 < sum_d:
        if sum_d % d == 0:
            return False
        d += 1
    return True

from random import shuffle

for n in range(70, 200):
    for _ in range(1000):
        s = list('1' * n + '2' * n)
        shuffle(s)
        s = '0' + ''.join(s) + '0'
        s2 = redaktor(s)
        if check_sum_digits(s2):
            print(n)
            break