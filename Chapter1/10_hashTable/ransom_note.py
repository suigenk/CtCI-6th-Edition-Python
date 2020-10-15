#!/bin/python3

import math
import os
import random
import re
import sys

def countFrequency(input_list: list):
    # Creating an empty dictionary.
    freq = {}
    for item in input_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # Count frequency of the words.
    magazine_freq = countFrequency(magazine)
    note_freq = countFrequency(note)

    # Flags to check True, False.
    flags = []

    # Check key and value for each dict.
    for key, value in note_freq.items():
        # Check whether key is in magazine_freq or not.
        if key not in magazine_freq.keys():
            flags.append(False)
        # Check whether value exceeds magazine_freq's value or not.
        elif value > magazine_freq[key]:
            flags.append(False)
        # If we meet these condition, flag is True.
        else:
            flags.append(True)

    # Check flags.
    if False in flags:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    # Process input.
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)
