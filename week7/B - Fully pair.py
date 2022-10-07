"""B - Fully pair?"""


def main(message):
    """Input"""
    again = 0
    used = ""
    for i in message:
        if used.count(i) != 0:
            continue
        total = 0
        total = message.count(i)
        if total%2 != 0:
            again += 1
            used += i
            print(i, end="")

    if again == 0:
        print("fully paired")
main(input())
