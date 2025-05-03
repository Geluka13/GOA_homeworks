def even_squares(numbers):   
    result = []
    for num in numbers:
        if (lambda x: x % 2 == 0)(num):
            result.append((lambda x: x ** 2)(num))
    return result
nums = [1, 2, 3, 4, 5, 6]
print(even_squares(nums))