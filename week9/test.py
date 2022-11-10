"""GCD_v1"""

import json
def main():
    """Input"""
    num = input()
    box = {}
    for i in num:
        if i in box:
            box[i] += 1
        else:
            box[i] = 1
    print(box)
main()
