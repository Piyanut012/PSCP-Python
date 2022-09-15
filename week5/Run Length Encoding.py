"""Run Length Encoding"""

def main(message):
    """Input"""
    count = 0
    check = message[0]
    for i in message:
        if i == check:
            count += 1
        else:
            print("%d%s" % (count, check), end="")
            count = 1
            check = i
    print("%d%s" % (count, check))

main(input())
