"""Sequence N"""

def main(num):
    """Input"""
    print("*" + " " * (num-2) + "*")
    for i in range(0, num-2, 1):
        print("*" + " " * (i) + "*" + " " * (num-3-i) + "*")
    print("*" + " " * (num-2) + "*")

main(int(input()))
