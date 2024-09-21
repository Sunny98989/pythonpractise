# import random
#
# #generate a list of 10 random integers between 1 and 10.
# random_order = [random.randint(1, 10) for i in range(10)]
#
# print(random_order)
# #but this repeats numbers : [5, 6, 8, 5, 3, 5, 5, 3, 10, 4]

import random


def numberGenerator(length):
    numbers = list(range(length))  # Generate indices based on the length of the password
    random_order = []

    for i in range(len(numbers)):
        index = random.randint(0, len(numbers) - 1)
        random_order.append(numbers.pop(index))

    return random_order
