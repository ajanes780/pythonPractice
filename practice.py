# print("Hello Aaron ")

# for item in [1,2,3,4,5,6,7]:
#   print(item)

user = {"name": "Golem", "age": 5006, "can_swim": False}

# for item in user.items():
#   print(item)


# for item in user.values():
#   print(item)


# for key, value in user.items():
#   if key == "name":
#     print(value)

# my_list= [1,2,3,4,5,6,7,8,9]

# count = 0
# for item in my_list:
#   count += item
#   print(count)


# my_range = list(range(10, 0 ,-2))
# # print(my_range)

# for _ in my_range:
#   print(_)


# enumerate
# for i, char in enumerate(list(range(100))):
#   if char == 50:
#     print(f"this is the index of 50 is:, {i}")

# while loop

# while True:
#     response = input("Say something: ")
#     if response == "bye":
#         print(response)
#     break

# #Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]

# for row in picture:
#     for pixel in row:
#         if not pixel:
#             print(" ", end=" ")
#         elif pixel:
#             print("*", end=" ")
#     print(" ")


#  sets
# some_list = ["a", "b", "b", "c", "d", "m", "n", "n"]

# # new_list = list(set(some_list))
# # print(new_list)
# # # with out a set
# answer = []
# #  with out a set
# for item in some_list:
#     if item not in answer:
#         answer.append(item)

# print(answer)


# def say_hello():
#     response = input("Who are you ?")
#     print(f"Hello {response}")


# say_hello()
def checkDriverAge():
    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.
checkDriverAge()
