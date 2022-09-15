"""Left Arrow"""


def main():
    """Input"""
    weigth = int(input())
    high = int(input())
    half = high//2 + 1
    for i in range(1, high+1, 1):
        if i <= half:
            space = half - i
            print(" " * space, end="")
            print("*" * weigth, end="")
        else:
            space = i % half
            print(" " * space, end="")
            print("*" * weigth, end="")
        print()

main()
