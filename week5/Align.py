"""Align"""

import math
def main(size, position, message):
    """Input"""
    if position == "left":
        print(message + ' ' * (size - len(message)))
    elif position == "center":
        space_front = math.ceil((size - len(message))/2)
        space_back = int((size - len(message))/2)
        print(' ' * (space_front) + message + ' ' * space_back)
    else:
        print(' ' * (size - len(message)) + message)

main(int(input()), input(), input())
