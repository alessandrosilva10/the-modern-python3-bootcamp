def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)


sum_all_values(2, 2)
sum_all_values(2, 2, 6, 3, 6)

nums = (1, 2, 3, 5, 6, 7, 9)
nums1 = (range(0, 10000000))

sum_all_values(*nums)
sum_all_values(*nums1)
