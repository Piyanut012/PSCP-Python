"""Hamburger"""


def main():
    """Input"""
    left = int(input())
    right = int(input())

    print("|" * left + "*" * left*2, end="")
    print("*" * right*2 + "|" * right)

main()
