#!/usr/bin/env python3

def return_evens(num_list):
    ls = [num for num in num_list if num % 2 == 0]
    return ls


def make_exclamation(sentence_list):
    return [sen + "!" for sen in sentence_list]
