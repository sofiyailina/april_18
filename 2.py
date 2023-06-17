print('x y z w f1 f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x <= y) == (w or (not z))
                f2 = (x <= y) and ((not w) == z)
                if f2 == 0 and (f1 == 1 or f1 == 0):
                    print(x, y, z, w, int(f1), int(f2))