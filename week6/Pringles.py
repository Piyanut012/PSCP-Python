"""Pringles"""


def main(can1, lay, can2, finger):
    """Input"""

    lay_num = lay.count(")")
    if finger > len(lay) - 1:
        finger = len(lay) - 1
    lay_left = (lay[-(len(lay) - finger):]).count(")")
    print(lay_num - lay_left)
    if lay_left == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(can1)
    print(" " * finger, end="")
    print(lay[-(len(lay) - finger):])
    print(can2)

main(input(), input(), input(), int(input()))
