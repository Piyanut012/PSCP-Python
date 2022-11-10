"""HorizontalHistogram"""

def main():
    """Input"""
    message = input()
    box_small = {}
    box_big = {}
    count = 0
    for i in message:
        if i in box_big or i in box_small:
            continue
        count = message.count(i)
        if i.islower():
            box_small[i] = count
        else:
            box_big[i] = count
    box_small = dict(sorted(box_small.items()))
    box_big = dict(sorted(box_big.items()))

    def printt(items):
        """Item"""
        for key, value in items:
            print(key, ":", end=" ")
            for i in range(value):
                if i%5 == 0 and i != 0:
                    print("|", end="")
                print("-", end="")
            print()
    printt(box_small.items())
    printt(box_big.items())
main()
