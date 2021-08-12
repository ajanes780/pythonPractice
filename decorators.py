# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}

# decorator pattern
def authenticated(fn):
    def wrap_func(*args, **kwargs):
        for item in args:
            if item.get("valid"):
                print("Authorized")
                fn(*args, **kwargs)
            else:
                print("Not authorized")

    return wrap_func


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
