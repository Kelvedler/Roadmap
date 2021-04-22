my_list = [1, 2, 3, 4, 5, 6, 7, 8]


# def even_bool(num):
#     return num%2 == 0


evens = filter(lambda num: num % 2 == 0, my_list)
print(list(evens))
