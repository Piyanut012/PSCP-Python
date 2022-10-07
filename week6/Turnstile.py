"""Turnstile"""


def main():
    """Input"""
    total = 0
    key_before = ""
    while True:
        key_current = input()
        if key_current == "END":
            break
        if key_current == "C":
            key_before = "C"
        elif key_current == "P" and key_before == "C":
            total += 1
            key_before = ""

    print(total)



main()

