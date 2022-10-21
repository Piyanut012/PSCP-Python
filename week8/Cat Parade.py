"""Cat Parade"""


def main():
    """Input"""
    box = []
    while True:
        dog = input()
        doglist = dog.split(sep=", ")
        if dog == "END":
            break
        if dog == "IT'S A DOG":
            box.pop()
            continue
        box.extend(doglist)
    box2 = box[:]
    box.sort()
    before = ""
    for i in box:
        if before == i:
            continue
        before = i
        print(i, "%d %d" % (box2.index(i)+1, box2.count(i)))

main()
