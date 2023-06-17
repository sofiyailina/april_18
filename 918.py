nums = []
with open('09.csv') as f:
    for line in f:
        line_nums = [int(k) for k in line.split(',')]
        nums.append(line_nums)
nums_pool = []
for line in nums:
    nums_pool.extend(line)
print(nums_pool[:20])

good_line_count = 0
for line in nums:
    for n in line:
        check1 = line.count(n) == 1
        check2 = nums_pool.count(n) == 46
        if check1 and check2:
            good_line_count += 1
            break
print(good_line_count)

