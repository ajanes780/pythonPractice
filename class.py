# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("greyKitty", 2)
cat2 = Cat("blackKitty", 3)
cat3 = Cat("redKitty", 4)


# 2 Create a function that finds the oldest cat
def oldestCat(*args):
    oldest = 0
    oldest = max(cat1.age, cat2.age, cat3.age)
    print(f"The oldest cat is {oldest} years old")


oldestCat()
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
