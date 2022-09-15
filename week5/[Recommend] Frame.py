"""Frame"""


def main():
    """Input"""
    message = input()
    space = len(message) + 2
    print("*" * space)
    print("*%s*" % message)
    print("*" * space)

main()
