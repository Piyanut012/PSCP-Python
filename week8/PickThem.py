"""PickThem"""

import json
def main():
    """Input"""
    box = input()
    check = False
    for i in json.loads(box):
        if i%2 == 0:
            check = True
            print(i)
    if check == False:
        print("Nope")
main()
