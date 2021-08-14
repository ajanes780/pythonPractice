def fibonacci_number(num):

    if num:
        a = 0
        b = 1
        for i in range(num):
            yield a
            temp = a
            a = b
            b = temp + b
    else:
        return "Please Choose a number greater then 0"


my_list = [i for i in fibonacci_number(-1)]
print(my_list)
