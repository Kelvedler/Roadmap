def array_check(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


array1 = [1, 3, 3, 1, 5, 1, 2]
array2 = [1, 2, 5, 1, 2, 3, 4]
print(array_check(array1))
print(array_check(array2))


def string_bits(string):
    return string[::2]


print(string_bits('heelloolloo'))


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        if a[len(a) - len(b):] == b:
            return True
    elif len(b) > len(a):
        if b[len(b) - len(a):] == a:
            return True
    else:
        if a == b:
            return True
    return False


print(end_other('abc', 'xAbc'))


def double_char(string):
    doubled = ''
    for char in string:
        doubled += char * 2
    return doubled


print(double_char('hello string'))


def fix_teen(n):
    if 12 < n < 15 or 16 < n < 20:
        return 0
    else:
        return n


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


print(no_teen_sum(10, 13, 15))


def count_evens(nums):
    counter = 0
    for num in nums:
        if num % 2 == 0:
            counter += 1
    return counter


print(count_evens([2, 2, 3, 4, 4, 6]))
