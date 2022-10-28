"""Meteorite"""


def main(weight, tak, weight_little):
    """Input"""
    count = 0
    num = 0
    while True:
        if weight < weight_little:
            break
        weight = weight/tak
        count += 1*tak**num
        num += 1
    print(count)

main(float(input()), int(input()), float(input()))
