"""Key"""

def main(id_card):
    """Input"""
    ssum = 0
    last_3 = ""
    check = 0
    for i in id_card:
        ssum = ssum + int(i)
        check = check + 1
        if check > 10:
            last_3 = last_3 + i
    key = ssum + int(last_3) * 10
    if key / 10000 >= 1:
        key = key % 10000
    elif key < 1000:
        key = key + 1000
    print("%04d" % key)

main(input())
