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


def nthFibNumber(n):
    fibNumbers = [1, 1]
    for x in range(n):
        fibNumbers += [fibNumbers[-1] + fibNumbers[-2]]
    return fibNumbers[n - 1]


print(nthFibNumber(100))
