#!/usr/bin/python3
def best_score(a_dictionary):
    std = None
    if a_dictionary:
        std = max(a_dictionary, key=a_dictionary.get)
    return(std)
