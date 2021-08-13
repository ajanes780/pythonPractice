def fibonacci_number(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fibonacci_number(21):
    print(f"fibonacci_number {x}")
