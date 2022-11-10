"""Safe"""

def main():
    """Input"""
    first = input()
    password = input()
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for i in range(len(first)):
        txt_first = character.index(first[i])
        txt_pass = character.index(password[i])
        diff = abs(txt_pass - txt_first)
        if diff > 13:
            count += 26 - (diff)
        else:
            count += diff
    print(count)
main()
