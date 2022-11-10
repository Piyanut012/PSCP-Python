"""BreachTheDoor"""

def main():
    """Input"""
    message = input()
    message = message.split()
    count = 0
    txt = ""
    box = []
    for i in message:
        for j in i:
            if j.isalpha():
                count += 1
                txt += j
        if count > 6:
            box.append(txt)
        count = 0
        txt = ""
    print(*box)
main()
