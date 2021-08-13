def fibonacci_number(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


# for i in fibonacci_number(21):
#     print(i)


my_list = [i for i in fibonacci_number(21)]
print(my_list)
