#!/usr/bin/python3
def remove_char_at(str, n):
    letter  = ""
    for i in range(len(str)):
        if i != n:
            letter = letter + str[i]
    return (letter)
