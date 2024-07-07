def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


numbers = [5, 2, 8, 1, 9]
result = apply_all_func(numbers, min, max, len, sum, sorted)
print(result)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))