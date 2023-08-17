#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del_keys.append(key)
    for key in del_keys:
        del a_dictionary[key]
    return a_dictionary
