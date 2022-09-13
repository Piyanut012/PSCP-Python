"""Distinguish"""


def main():
    """Input"""
    value = float(input())
    if value > 180:
        print("You're hit the door edge.")
    elif value <= 180:
        print("Nothing happens.")

main()
