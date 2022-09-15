"""Future Message"""


def main():
    """Input"""
    message = input()
    if message.islower():
        print("Lowercase")
    elif message.isupper():
        print("Uppercase")
    elif message.istitle():
        print("Title")
    elif message.isspace():
        print("Space")
    elif message.isdecimal():
        print("Number")
    else:
        print("Other")
main()
