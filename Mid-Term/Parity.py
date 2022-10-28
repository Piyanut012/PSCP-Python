"""Parity"""

def main(message, choize):
    """Input"""
    count = 0
    for i in message:
        if i == "1":
            count += 1
    if (choize == "Even" and count%2 == 0) or (choize == "Odd" and count%2 == 1):
        print(message + "0")
    else:
        print(message + "1")

main(input(), input())
