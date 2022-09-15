"""Virus I"""


def main():
    """Input"""
    message = input()
    body = 0
    for i in message:
        if i == "o":
            body += 1
    print(body)

main()
