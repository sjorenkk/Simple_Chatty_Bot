import math


def new_math_factorial(__x):
    print("Don't cheat!")


math.factorial = new_math_factorial


# don't delete this line, please
math.factorial(23)