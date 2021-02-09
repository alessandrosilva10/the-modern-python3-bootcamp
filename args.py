def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num

    return total


print(sum_all_nums(1, 2, 3))


def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are"


print(ensure_correct_info(1, True, "Steele", "Colt"))
print(ensure_correct_info(1, True, "Steele", "Cold"))

