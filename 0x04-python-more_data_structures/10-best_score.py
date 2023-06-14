#!/usr/bin/python3
def best_score(a_dictionary):
    # task 10 : return key of highest val
    if a_dictionary is None:
        return None
    # get first key of dict
    bst_score = list(a_dictionary.keys())[0]
    for ky, val in a_dictionary.items():
        bst_score = ky if val > a_dictionary[bst_score] else bst_score
    return bst_score


"""
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
"""
