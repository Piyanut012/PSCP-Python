"""RightArrow"""


def main():
    """Input"""
    width = int(input())
    high = int(input())
    for i in range(0, high):
        if i <= (high-1)/2:
            print(" " * i, end="")
            print("*" * width, end="")
        else:
            i = high-1-i
            print(" " * i, end="")
            print("*" * width, end="")
        print()

main()

