#!/usr/bin/python3
def weight_average(my_list=[]):
    # task 13 (100-w*.py) : weighted avg. of all integers
    # in tuple (<score>, <weight>)
    # avg = sum of all (score * weight) / sum of (weights)
    sum = 0
    dividor = 0
    for tupl in my_list:
        sum += (tupl[0] * tupl[1])
        dividor += tupl[1]
    return sum / dividor if sum else 0


"""
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
"""
