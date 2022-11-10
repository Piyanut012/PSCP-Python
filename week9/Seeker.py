"""Seeker"""

def main():
    """Input"""
    message = input()
    ans = 0
    for i in message:
        if not i.isnumeric():
            message = message.replace(i, " ")
    message = message.split()
    for i in message:
        ans += int(i)
    print(ans)
main()
