def do_stuff(num=0):
    try:
        if num and not num == " " or num == 0:
            return int(num) + 5
        else:
            return "Please use a number"
    except ValueError as err:
        return err
