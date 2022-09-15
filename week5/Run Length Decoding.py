"""Run Length Decoding"""

def main(message):
    """Input"""
    num = ""
    for i in message:
        if i.isnumeric():
            num = num + i
        else:
            print(i * int(num), end="")
            num = ""

main(input())
