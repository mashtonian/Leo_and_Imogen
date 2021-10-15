# print("Hello Imogen")
# print("Hello Leo")
#
# print("This is a list of numbers: ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# # We can add things to the end of the list:
#
# listOfNumbers = [10, 20, 30]
# print(listOfNumbers)
#
# listOfNumbers += [40]
# print(listOfNumbers)
#
# # We can access items in the list:
# # From the beginning:
# print(listOfNumbers[0], listOfNumbers[1], listOfNumbers[2], listOfNumbers[3])
#
# # Or from the end:
# print(listOfNumbers[-1], listOfNumbers[-2])
from functools import lru_cache


def fibRecursive(n, fib_values={1: 1, 2: 1}):
    if n in fib_values:
        result = fib_values[n]
    else:
        result = fibRecursive(n - 1, fib_values) + fibRecursive(n - 2, fib_values)
        fib_values.setdefault(n, result)
    return result


@lru_cache(maxsize=None)
def fibRecursiveCached(n):
    if n < 3:
        return 1
    else:
        return fibRecursiveCached(n - 1) + fibRecursiveCached(n - 2)


fibRecursive(5)
