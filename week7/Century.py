"""Century"""

import math
def main(num):
    """Input"""
    for _ in range(num):
        message = input()
        typez = message[:4]
        years = int(message[5:])

        if typez == "B.E.":
            if years > 543:
                century = math.ceil((years-543)/100)
                print(century)
            else:
                print("ERROR")
        else:
            century = math.ceil((years)/100)
            print(century)

main(int(input()))

